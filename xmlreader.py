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
    rfc_busqueda = st.text_input('Ingresa el RFC de la sociedad que deseas filtrar:', max_chars=13)

    if st.button('Procesar') and uploaded_files:
        data_parse_xml4 = []
        data_parse_xml33 = []
        data_parse_xml32 = []
        data_parse_xmlcomp33 = []
        data_parse_xmlcomp40 = []
        xml_files_not_processed_parse_xml4 = []
        xml_files_not_processed_parse_xml33 = []
        xml_files_not_processed_parse_xml32 = []
        xml_files_not_processed_parse_xmlcomp33 = []
        xml_files_not_processed_parse_xmlcomp40 = []

        for uploaded_file in uploaded_files:
            if uploaded_file:
                with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
                    xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]

                    for xml_file in xml_files:
                        xml_content = zip_ref.read(xml_file)
                        try:
                            xml_data_parse_xml4 = parse_xml4(xml_content)
                            data_parse_xml4.append(xml_data_parse_xml4)
                        except Exception as e:
                            xml_files_not_processed_parse_xml4.append(xml_file)

                        try:
                            xml_data_parse_xml33 = parse_xml33(xml_content)
                            data_parse_xml33.append(xml_data_parse_xml33)
                        except Exception as e:
                            xml_files_not_processed_parse_xml33.append(xml_file)

                        try:
                            xml_data_parse_xml32 = parse_xml32(xml_content)
                            data_parse_xml32.append(xml_data_parse_xml32)
                        except Exception as e:
                            xml_files_not_processed_parse_xml32.append(xml_file)

                        try:
                            xml_data_parse_xmlcomp33 = parse_xmlcomp33(xml_content)
                            data_parse_xmlcomp33.append(xml_data_parse_xmlcomp33)
                        except Exception as e:
                            xml_files_not_processed_parse_xmlcomp33.append(xml_file)

                        try:
                            xml_data_parse_xmlcomp40 = parse_xmlcomp40(xml_content)
                            data_parse_xmlcomp40.append(xml_data_parse_xmlcomp40)
                        except Exception as e:
                            xml_files_not_processed_parse_xmlcomp40.append(xml_file)

        total_archivos = len(data_parse_xml4) + len(data_parse_xml33) + len(data_parse_xml32) + len(data_parse_xmlcomp33) + len(data_parse_xmlcomp40)
        st.info(f'Total de archivos cargados: {total_archivos}')

        df_parse_xml4 = pd.DataFrame(data_parse_xml4)
        df_parse_xml33 = pd.DataFrame(data_parse_xml33)
        df_parse_xml32 = pd.DataFrame(data_parse_xml32)
        df_parse_xmlcomp33 = pd.DataFrame(data_parse_xmlcomp33)
        df_parse_xmlcomp40 = pd.DataFrame(data_parse_xmlcomp40)

        if xml_files_not_processed_parse_xml4:
            df_not_processed_parse_xml4 = pd.DataFrame({'Archivo no procesado': xml_files_not_processed_parse_xml4})
            st.dataframe(df_not_processed_parse_xml4)

        if xml_files_not_processed_parse_xml33:
            df_not_processed_parse_xml33 = pd.DataFrame({'Archivo no procesado': xml_files_not_processed_parse_xml33})
            st.dataframe(df_not_processed_parse_xml33)

        if xml_files_not_processed_parse_xml32:
            df_not_processed_parse_xml32 = pd.DataFrame({'Archivo no procesado': xml_files_not_processed_parse_xml32})
            st.dataframe(df_not_processed_parse_xml32)

        st.dataframe(df_parse_xml33)
        st.dataframe(df_parse_xml4)
        st.dataframe(df_parse_xml32)

if __name__ == '__main__':
    main()
