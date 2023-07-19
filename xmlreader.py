import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
import os
import zipfile
import time


def extract_xml_files(zip_files):
    extracted_files = []

    for zip_file in zip_files:
        with zipfile.ZipFile(zip_file, 'r') as zf:
            # Extract XML files to a temporary folder
            extract_folder = 'temp'
            zf.extractall(extract_folder)
            
            # Add extracted XML files to the list
            for root, _, files in os.walk(extract_folder):
                for file in files:
                    if file.endswith('.xml'):
                        extracted_files.append(os.path.join(root, file))

    return extracted_files



def cfdv40(xml_file):
    # Parsing XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Namespace dictionary
    namespaces = {
        'cfdi': 'http://www.sat.gob.mx/cfd/4',
        'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
        'pago10': 'http://www.sat.gob.mx/Pagos'
    }

    # Extracting desired data from XML
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


def cfdv33(xml_file):
    # Parsing XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Namespace dictionary
    namespaces = {
        'cfdi': 'http://www.sat.gob.mx/cfd/3',
        'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
        'pago10': 'http://www.sat.gob.mx/Pagos'
    }

    # Extracting desired data from XML
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
    impuestos = root.find('', namespaces=namespaces).attrib.get('Rfc', '')

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
        'fecha_emision': fecha_emision,
        'impuestos': impuestos
    }


def cfdcomp33(xml_file):
    # Parsing XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Namespace dictionary
    ns = {
        "cfdi": "http://www.sat.gob.mx/cfd/3",
        "pago10": "http://www.sat.gob.mx/Pagos",
        "tfd": "http://www.sat.gob.mx/TimbreFiscalDigital"
    }

    # Extracting desired data from XML
    pago_element = root.find("cfdi:Complemento/pago10:Pagos/pago10:Pago", ns)

    fecha_pago = pago_element.attrib.get("FechaPago")
    forma_pago = pago_element.attrib.get("FormaDePagoP")
    moneda_pago = pago_element.attrib.get("MonedaP")
    monto = pago_element.attrib.get("Monto")
    tipo_de_comprobante = root.attrib.get('TipoDeComprobante', '')

    doc_relacionado_element = pago_element.find("pago10:DoctoRelacionado", ns)
    id_documento = doc_relacionado_element.attrib.get("IdDocumento")
    moneda_dr = doc_relacionado_element.attrib.get("MonedaDR")
    metodo_pago_dr = doc_relacionado_element.attrib.get("MetodoDePagoDR")
    num_parcialidad = doc_relacionado_element.attrib.get("NumParcialidad")
    imp_saldo_ant = doc_relacionado_element.attrib.get("ImpSaldoAnt")
    imp_pagado = doc_relacionado_element.attrib.get("ImpPagado")
    imp_saldo_insoluto = doc_relacionado_element.attrib.get("ImpSaldoInsoluto")

    return {
        "version": root.attrib.get("Version"),
        "tipo comprobante": root.attrib.get('TipoDeComprobante'),
        "Fecha": root.attrib.get("Fecha"),
        "RFC emisor": root.find("cfdi:Emisor", ns).attrib.get("Rfc"),
        "Nombre emisor": root.find("cfdi:Emisor", ns).attrib.get("Nombre"),
        "RFC receptor": root.find("cfdi:Receptor", ns).attrib.get("Rfc"),
        "Nombre receptor": root.find("cfdi:Receptor", ns).attrib.get("Nombre"),
        "uso_cfdi": root.find("cfdi:Receptor", ns).attrib.get("UsoCFDI"),
        "UUID": root.find("cfdi:Complemento/tfd:TimbreFiscalDigital", ns).attrib.get("UUID"),
        "FechaPago": fecha_pago,
        "FormaDePagoP": forma_pago,
        "MonedaP": moneda_pago,
        "Monto": monto,
        "IdDocumento": id_documento,
        "MonedaDR": moneda_dr,
        "MetodoDePagoDR": metodo_pago_dr,
        "NumParcialidad": num_parcialidad,
        "ImpSaldoAnt": imp_saldo_ant,
        "ImpPagado": imp_pagado,
        "ImpSaldoInsoluto": imp_saldo_insoluto
    }


def cfdcomp40(xml_file):
    # Parsing XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Namespace dictionary
    ns = {
        "cfdi": "http://www.sat.gob.mx/cfd/4",
        "pago20": "http://www.sat.gob.mx/Pagos20",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "tfd": "http://www.sat.gob.mx/TimbreFiscalDigital"
    }

    # Extracting desired data from XML
    pago_element = root.find("cfdi:Complemento/pago20:Pagos/pago20:Pago", ns)

    fecha_pago = pago_element.attrib.get("FechaPago")
    forma_pago = pago_element.attrib.get("FormaDePagoP")
    moneda_pago = pago_element.attrib.get("MonedaP")
    monto = pago_element.attrib.get("Monto")

    doc_relacionado_element = pago_element.find("pago20:DoctoRelacionado", ns)
    id_documento = doc_relacionado_element.attrib.get("IdDocumento")
    moneda_dr = doc_relacionado_element.attrib.get("MonedaDR")
    metodo_pago_dr = doc_relacionado_element.attrib.get("MetodoDePagoDR")
    num_parcialidad = doc_relacionado_element.attrib.get("NumParcialidad")
    imp_saldo_ant = doc_relacionado_element.attrib.get("ImpSaldoAnt")
    imp_pagado = doc_relacionado_element.attrib.get("ImpPagado")
    imp_saldo_insoluto = doc_relacionado_element.attrib.get("ImpSaldoInsoluto")

    return {
        "version": root.attrib.get("Version"),
        "Fecha": root.attrib.get("Fecha"),
        "RFC emisor": root.find("cfdi:Emisor", ns).attrib.get("Rfc"),
        "Nombre emisor": root.find("cfdi:Emisor", ns).attrib.get("Nombre"),
        "RFC receptor": root.find("cfdi:Receptor", ns).attrib.get("Rfc"),
        "Nombre receptor": root.find("cfdi:Receptor", ns).attrib.get("Nombre"),
        "uso_cfdi": root.find("cfdi:Receptor", ns).attrib.get("UsoCFDI"),
        "UUID": root.find("cfdi:Complemento/tfd:TimbreFiscalDigital", ns).attrib.get("UUID"),
        "FechaPago": fecha_pago,
        "FormaDePagoP": forma_pago,
        "MonedaP": moneda_pago,
        "Monto": monto,
        "IdDocumento": id_documento,
        "MonedaDR": moneda_dr,
        "MetodoDePagoDR": metodo_pago_dr,
        "NumParcialidad": num_parcialidad,
        "ImpSaldoAnt": imp_saldo_ant,
        "ImpPagado": imp_pagado,
        "ImpSaldoInsoluto": imp_saldo_insoluto
    }

def main():
    st.title("XML Processing App")

    # Upload multiple zip files
    uploaded_files = st.file_uploader("Upload multiple zip files", accept_multiple_files=True)

    if st.button("Process"):
        if uploaded_files:
            # Extract XML files from zip files
            extracted_files = extract_xml_files(uploaded_files)
            st.dataframe(extracted_files)
            total_archivos = len(extracted_files)
            st.info(f'Total de archivos en la carpeta: {total_archivos}')

            start_time = time.time()
            

            data_parse_cfd40 = []
            data_parse_cfd33 = []
            data_parse_cfdcomp33 = []
            data_parse_cfdcomp40 = []
            cfd40_not_processed = []
            cfdv33_not_processed = []
            cfdcomp33_not_processed = []
            cfdcomp40_not_processed = []
            
            df_cfdv33 = pd.DataFrame()  # Inicializar df_parse_xml33 como un DataFrame vacío
            df_cfdv40 = pd.DataFrame()  # Inicializar df_parse_xml4 como un DataFrame vacío
            df_cfdcomp33 = pd.DataFrame()  # Inicializar df_parse_xmlcomp33 como un DataFrame vacío
            df_cfdcomp40 = pd.DataFrame()  # Inicializar df_parse_xmlcomp40 como un DataFrame vacío
            
            for xml_path in extracted_files:
                try:
                    xml_data_parse_cfdv33 = cfdv33(xml_path)
                    data_parse_cfd33.append(xml_data_parse_cfdv33)
                except Exception as e:
                    cfdv33_not_processed.append(xml_path)
            
                try:
                    xml_data_parse_cfd40 = cfdv40(xml_path)
                    data_parse_cfd40.append(xml_data_parse_cfd40)
                except Exception as e:
                    cfd40_not_processed.append(xml_path)

                try:
                    xml_data_parse_cfdcomp33 = cfdcomp33(xml_path)
                    data_parse_cfdcomp33.append(xml_data_parse_cfdcomp33)
                except Exception as e:
                    cfdcomp33_not_processed.append(xml_path)

                try:
                    xml_data_parse_cfdcomp40 = cfdcomp40(xml_path)
                    data_parse_cfdcomp40.append(xml_data_parse_cfdcomp40)
                except Exception as e:
                    cfdcomp40_not_processed.append(xml_path)

            end_time = time.time()
            processing_time = end_time - start_time
            processing_time_formatted = "{:.4f}".format(processing_time)
            st.info(f'Se encontraron un total de {total_archivos} archivos, los cuales fueron procesados en un tiempo total de: {processing_time_formatted} segundos')
            
            df_cfdv33 = pd.DataFrame(data_parse_cfd33)
            df_cfdv40 = pd.DataFrame(data_parse_cfd40)
            df_cfdcomp33 = pd.DataFrame(data_parse_cfdcomp33)
            df_cfdcomp40 = pd.DataFrame(data_parse_cfdcomp40)
            
            st.caption('CFDIs Version 3.3')
            st.write(df_cfdv33.shape)
            st.dataframe(df_cfdv33)
            
            st.caption('CFDIs Version 4.0')
            st.write(df_cfdv40.shape)
            st.dataframe(df_cfdv40)

            st.caption('Complementos de Pago Version 3.3')
            st.write(df_cfdcomp33.shape)
            st.dataframe(df_cfdcomp33)

            st.caption('Complementos de Pago Version 4.0')
            st.write(df_cfdcomp40.shape)
            st.dataframe(df_cfdcomp40)


if __name__ == "__main__":
    main()
