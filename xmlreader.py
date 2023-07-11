import streamlit as st
import zipfile
import xml.etree.ElementTree as ET

def parse_xml4(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    namespaces = {
        'cfdi': 'http://www.sat.gob.mx/cfd/4',
        'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
        'pago10': 'http://www.sat.gob.mx/Pagos'
    }

    version = root.attrib.get('Version', '')
    forma_de_pago = root.attrib.get('FormaPago', '')
    regimen = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('RegimenFiscal', '')
    tipo_de_comprobante = root.attrib.get('TipoDeComprobante', '')
    rfc_emisor = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Rfc', '')
    nombre_emisor = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Nombre', '')
    rfc_receptor = root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Rfc', '')
    nombre_receptor = root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Nombre', '')
    subtotal = root.attrib.get('SubTotal', '')
    total = root.attrib.get('Total', '')
    uuid = root.find('cfdi:Complemento/tfd:TimbreFiscalDigital', namespaces=namespaces).attrib.get('UUID', '')
    fecha_emision = root.attrib.get('Fecha', '')

    return {
        'version': version,
        'forma_de_pago': forma_de_pago,
        'regimen': regimen,
        'tipo_de_comprobante': tipo_de_comprobante,
        'rfc_emisor': rfc_emisor,
        'nombre_emisor': nombre_emisor,
        'rfc_receptor': rfc_receptor,
        'nombre_receptor': nombre_receptor,
        'subtotal': subtotal,
        'total': total,
        'uuid': uuid,
        'fecha_emision': fecha_emision
    }

def parse_xml33(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    namespaces = {
        'cfdi': 'http://www.sat.gob.mx/cfd/3',
        'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
        'pago10': 'http://www.sat.gob.mx/Pagos'
    }

    version = root.attrib.get('Version', '')
    forma_de_pago = root.attrib.get('FormaPago', '')
    regimen = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('RegimenFiscal', '')
    tipo_de_comprobante = root.attrib.get('TipoDeComprobante', '')
    rfc_emisor = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Rfc', '')
    nombre_emisor = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Nombre', '')
    rfc_receptor = root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Rfc', '')
    nombre_receptor = root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Nombre', '')
    subtotal = root.attrib.get('SubTotal', '')
    total = root.attrib.get('Total', '')
    uuid = root.find('cfdi:Complemento/tfd:TimbreFiscalDigital', namespaces=namespaces).attrib.get('UUID', '')
    fecha_emision = root.attrib.get('Fecha', '')
    
    return {
        'version': version,
        'forma_de_pago': forma_de_pago,
        'regimen': regimen,
        'tipo_de_comprobante': tipo_de_comprobante,
        'rfc_emisor': rfc_emisor,
        'nombre_emisor': nombre_emisor,
        'rfc_receptor': rfc_receptor,
        'nombre_receptor': nombre_receptor,
        'subtotal': subtotal,
        'total': total,
        'uuid': uuid,
        'fecha_emision': fecha_emision
    }

def main():
    uploaded_files = st.file_uploader('Cargar archivos ZIP', accept_multiple_files=True, type='zip')

    for uploaded_file in uploaded_files:
        if uploaded_file:
            with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
                xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]

                for xml_file in xml_files:
                    xml_content = zip_ref.read(xml_file)
                    data = extract_xml_data(xml_content)

                    # Haz lo que desees con los datos extraídos del XML
                    st.write(data)

if __name__ == '__main__':
    main()
