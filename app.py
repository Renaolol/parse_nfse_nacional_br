import xml.etree.ElementTree as ET
ns = {'ns':'http://www.sped.fazenda.gov.br/nfse'}
def parse_nfse(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    #Local da prestação do serviço
    loc_prestacao = root.find('ns:infNFSe//ns:xLocPrestacao',ns).text if root.find('ns:infNFSe//ns:xLocPrestacao',ns) is not None else "Não informado"
    #Local de incidência do ISSQN
    loc_incid_issqn = root.find('ns:infNFSe//ns:xLocIncid',ns).text if root.find('ns:infNFSe//ns:xLocIncid',ns) is not None else "Não informado"
    #Nome do Emitente
    emitente =  root.find('ns:infNFSe//ns:emit//ns:xNome',ns).text if root.find('ns:infNFSe//ns:emit//ns:xNome',ns) is not None else "Não Informado"
    #Nome do Destinatário da NFSe
    destinatario = root.find('ns:infNFSe//ns:toma//ns:xNome',ns).text if root.find('ns:infNFSe//ns:toma//ns:xNome',ns) is not None else "Não Informado"
    #Valor Liquido da NFSe
    valor_liquido = float(root.find('ns:infNFSe//ns:valores//ns:vLiq',ns).text) if root.find('ns:infNFSe//ns:valores//ns:vLiq',ns) is not None else 0.00
    #Valor Retido da NFSe
    valor_retido = float(root.find('ns:infNFSe//ns:valores//ns:vTotalRet',ns).text) if root.find('ns:infNFSe//ns:valores//ns:vTotalRet',ns) is not None else 0.00
    #Valor total da NFSe
    valor_servico = float(root.find('ns:infNFSe//ns:valores//ns:vServ',ns).text) if root.find('ns:infNFSe//ns:valores//ns:vServ',ns) is not None else 0.00
    #IMPOSTOS ----------
    #ISSQN
    iss = float(root.find('ns:infNFSe//ns:valores//ns:vISSQN',ns).text) if root.find('ns:infNFSe//ns:valores//ns:vISSQN',ns) is not None else 0.00
    #PIS
    pis = float(root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:piscofins//ns:vPis',ns).text) if root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:piscofins//ns:vPis',ns) is not None else 0.00
    #COFINS
    cofins = float(root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:piscofins//ns:vCofins',ns).text) if root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:piscofins//ns:vCOfins',ns) is not None else 0.00
    #RETENÇÕES ----------
    #CP//INSS
    ret_cp = float(root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:vRetCP',ns).text) if root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:vRetCP',ns) is not None else 0.00
    #IRRF
    ret_irrf = float(root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:vRetIRRF',ns).text) if root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:vRetIRRF',ns) is not None else 0.00
    #CSLL
    ret_csll = float(root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:vRetCSLL',ns).text) if root.find('ns:infNFSe//ns:valores//ns:tribFed//ns:vRetCSLL',ns) is not None else 0.00

    return loc_prestacao, loc_incid_issqn, emitente, destinatario, valor_liquido, valor_retido, valor_servico, iss, pis, cofins, ret_cp, ret_irrf, ret_csll

