import streamlit as st
import os
import xml.etree.ElementTree as ET

def extract_xml_data(xml_content):
    # Lógica para extraer información del XML y devolver un diccionario
    # Personaliza esta función según tus necesidades
    root = ET.fromstring(xml_content)
    data = {
        'version': root.attrib.get('Version', ''),
        'forma_de_pago': root.attrib.get('FormaPago', ''),
        'regimen': root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('RegimenFiscal', ''),
        'tipo_de_comprobante': root.attrib.get('TipoDeComprobante', ''),
        'rfc_emisor': root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Rfc', ''),
        'nombre_emisor': root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Nombre', ''),
        'rfc_receptor': root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Rfc', ''),
        'nombre_receptor': root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Nombre', ''),
        'subtotal': root.attrib.get('SubTotal', ''),
        'total': root.attrib.get('Total', ''),
        'uuid': root.find('cfdi:Complemento/tfd:TimbreFiscalDigital', namespaces=namespaces).attrib.get('UUID', ''),
        'fecha_emision': root.attrib.get('Fecha', '')
    }
    return data

def main():
    uploaded_folder = st.file_uploader('Cargar carpeta', type='folder')

    if uploaded_folder:
        folder_path = st.text_input('Ruta de la carpeta:', value=uploaded_folder.name)
        xml_files = [file for file in os.listdir(folder_path) if file.endswith('.xml')]

        for xml_file in xml_files:
            xml_content = open(os.path.join(folder_path, xml_file), 'rb').read()
            data = extract_xml_data(xml_content)

            # Haz lo que desees con los datos extraídos del XML
            st.write(data)

if __name__ == '__main__':
    main()
