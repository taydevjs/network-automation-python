def gerador_l2l_final():
    print("--- GERADOR L2L: PROVISIONAMENTO + SAP + BRIDGE ---")
    
    # Coleta de dados
    vlan_stacked_full = input("VLAN ID Stacked completa (ex: 1802:0): ")
    vpls_id = input("ID do VPLS / Master (ex: 581, 582, 583): ")
    name_vlan = input("Name da VLAN (ex: L2L-BSBSEG-UBS12-CEILANDIA-166728): ")
    desc_vpls = input("Description da VPLS (ex: L2L-BSBSEG-190384-CAESB): ")
    posicao_ont = input("Posicionamento ONT (ex: 1/1/1/15/10): ")
    sernum = input("Serial Number ONT (ex: ALCL:B2893D24): ")
    vlan_pon_bridge = input("VLAN ID Bridge Final (ex: 1800:0): ")

    # Lógica para extrair Rack/Shelf/Slot e a VLAN pura para o SAP
    p = posicao_ont.split('/')
    vlan_pura = vlan_stacked_full.split(':')[0]
    
    try:
        # Monta o SAP no padrão sap lt:1/1/10:1802
        sap_formatted = f"lt:{p[0]}/{p[1]}/{p[4]}:{vlan_pura}" 
    except IndexError:
        sap_formatted = "lt:ERRO/NA/POSICAO:VLAN"

    script = f"""
# 1. CRIAR VLAN E VPLS
info configure vlan flat
configure vlan id stacked:{vlan_stacked_full} mode cross-connect name "{name_vlan}" l2cp-transparent in-qos-prof-name name:HSI ipv4-mcast-ctrl ipv6-mcast-ctrl

configure service
    vpls {vpls_id} customer 1 create
        description "{desc_vpls}"
        stp
            shutdown
        exit
    

# 2. ASSOCIAR SAP A VPLS
configure service
vpls {vpls_id}
sap {sap_formatted} create
description "{desc_vpls}"
no shutdown
exit

# 3. COLOCAR EM BRIDGE (PROVISIONAMENTO VEIP)
configure equipment ont interface {posicao_ont} desc1 "{name_vlan}" sernum {sernum} pland-cfgfile1 auto dnload-cfgfile1 auto sw-ver-pland auto
configure equipment ont interface {posicao_ont} admin-state up optics-hist enable
configure equipment ont slot {posicao_ont}/60 planned-card-type veip plndnumdataports 1 plndnumvoiceports 0
configure interface port uni:{posicao_ont}/14/1 admin-up
configure qos interface {posicao_ont}/14/1 upstream-queue 0 bandwidth-profile name:HSI_200M_UP
configure bridge port {posicao_ont}/14/1
vlan-id 100 tag single-tagged
exit all

# 4. CONFIGURAÇÃO BRIDGE ETHERNET FINAL
configure equipment ont slot {posicao_ont}/1 planned-card-type ethernet plndnumdataports 4 plndnumvoiceports 0
configure interface port uni:{posicao_ont}/1/4 admin-up
configure qos interface {posicao_ont}/1/4 upstream-queue 0 bandwidth-profile name:HSI_200M_UP
configure qos interface {posicao_ont}/1/4 upstream-queue 0 shaper-profile name:HSI_200M_DOWN
configure qos interface {posicao_ont}/1/4 queue 0 shaper-profile name:HSI_200M_DOWN
configure bridge port {posicao_ont}/1/4 max-unicast-mac 64 max-committed-mac 1
configure bridge port {posicao_ont}/1/4 vlan-id stacked:{vlan_pon_bridge}
configure bridge port {posicao_ont}/1/4 pvid stacked:{vlan_pon_bridge}
exit all
"""
    print("\n" + "="*60)
    print("SCRIPT GERADO COM SUCESSO:")
    print("="*60)
    print(script)

gerador_l2l_final()