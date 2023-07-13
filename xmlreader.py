import os
import zipfile
import pandas as pd
import xml.etree.ElementTree as ET
import streamlit as st
import tempfile


def extract_xml_data(xml_file):
    namespaces = {
        'cfdi': 'http://www.sat.gob.mx/cfd/3',
        'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
        'pago10': 'http://www.sat.gob.mx/Pagos'
    }

    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = {}
    data['Version'] = root.attrib.get('Version', '')
    data['FormaPago'] = root.attrib.get('FormaPago', '')
    data['RegimenFiscal'] = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('RegimenFiscal', '')
    data['TipoDeComprobante'] = root.attrib.get('TipoDeComprobante', '')
    data['RfcEmisor'] = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Rfc', '')
    data['NombreEmisor'] = root.find('cfdi:Emisor', namespaces=namespaces).attrib.get('Nombre', '')
    data['RfcReceptor'] = root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Rfc', '')
    data['NombreReceptor'] = root.find('cfdi:Receptor', namespaces=namespaces).attrib.get('Nombre', '')
    data['SubTotal'] = root.attrib.get('SubTotal', '')
    data['Total'] = root.attrib.get('Total', '')
    data['UUID'] = root.find('cfdi:Complemento/tfd:TimbreFiscalDigital', namespaces=namespaces).attrib.get('UUID', '')
    data['FechaEmision'] = root.attrib.get('Fecha', '')

    conceptos = []
    impuestos = []

    for concepto in root.findall('cfdi:Conceptos/cfdi:Concepto', namespaces=namespaces):
        concepto_data = {
            'ClaveProdServ': concepto.attrib.get('ClaveProdServ', ''),
            'NoIdentificacion': concepto.attrib.get('NoIdentificacion', ''),
            'Cantidad': concepto.attrib.get('Cantidad', ''),
            'ClaveUnidad': concepto.attrib.get('ClaveUnidad', ''),
            'Descripcion': concepto.attrib.get('Descripcion', ''),
            'Unidad': concepto.attrib.get('Unidad', ''),
            'ValorUnitario': concepto.attrib.get('ValorUnitario', ''),
            'Importe': concepto.attrib.get('Importe', ''),
            'Descuento': concepto.attrib.get('Descuento', '')
        }
        conceptos.append(concepto_data)

        for impuesto in concepto.findall('cfdi:Impuestos/cfdi:Traslados/cfdi:Traslado', namespaces=namespaces):
            impuesto_data = {
                'Base': impuesto.attrib.get('Base', ''),
                'Impuesto': impuesto.attrib.get('Impuesto', ''),
                'TipoFactor': impuesto.attrib.get('TipoFactor', ''),
                'TasaOCuota': impuesto.attrib.get('TasaOCuota', ''),
                'Importe': impuesto.attrib.get('Importe', '')
            }
            impuestos.append(impuesto_data)

    return data, conceptos, impuestos


def process_zip_files(zip_files):
    xml_data = []
    temp_dir = tempfile.mkdtemp()  # Create a temporary directory in the cache

    for file_data in zip_files:
        file_name = file_data.name
        file_path = os.path.join(temp_dir, file_name)
        with open(file_path, 'wb') as f:
            f.write(file_data.getbuffer())

        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        xml_files = [f for f in zip_ref.namelist() if f.endswith('.xml')]
        for xml_file in xml_files:
            xml_path = os.path.join(temp_dir, xml_file)
            data, conceptos, impuestos = extract_xml_data(xml_path)
            xml_data.append({
                'File': xml_file,
                'Data': data,
                'Conceptos': conceptos,
                'Impuestos': impuestos
            })

    return xml_data


def main():
    st.title("XML Data Extraction")

    zip_files = st.file_uploader("Upload ZIP Files", accept_multiple_files=True)
    if st.button("Process") and zip_files:
        xml_data = process_zip_files(zip_files)

        if not xml_data:
            st.warning("No XML files found!")

        rows = []
        for xml in xml_data:
            file = xml['File']
            data = xml['Data']
            conceptos = xml['Conceptos']
            impuestos = xml['Impuestos']
            for concepto in conceptos:
                for impuesto in impuestos:
                    row = {
                        'File': file,
                        'Version': data['Version'],
                        'FormaPago': data['FormaPago'],
                        'RegimenFiscal': data['RegimenFiscal'],
                        'TipoDeComprobante': data['TipoDeComprobante'],
                        'RfcEmisor': data['RfcEmisor'],
                        'NombreEmisor': data['NombreEmisor'],
                        'RfcReceptor': data['RfcReceptor'],
                        'NombreReceptor': data['NombreReceptor'],
                        'SubTotal': data['SubTotal'],
                        'Total': data['Total'],
                        'UUID': data['UUID'],
                        'FechaEmision': data['FechaEmision'],
                        'ClaveProdServ': concepto['ClaveProdServ'],
                        'NoIdentificacion': concepto['NoIdentificacion'],
                        'Cantidad': concepto['Cantidad'],
                        'ClaveUnidad': concepto['ClaveUnidad'],
                        'Descripcion': concepto['Descripcion'],
                        'Unidad': concepto['Unidad'],
                        'ValorUnitario': concepto['ValorUnitario'],
                        'Importe': concepto['Importe'],
                        'Descuento': concepto['Descuento'],
                        'Base': impuesto['Base'],
                        'Impuesto': impuesto['Impuesto'],
                        'TipoFactor': impuesto['TipoFactor'],
                        'TasaOCuota': impuesto['TasaOCuota'],
                        'ImporteImpuesto': impuesto['Importe']
                    }
                    rows.append(row)

        if rows:
            df = pd.DataFrame(rows)
            st.write(df)
        else:
            st.warning("No data to display!")


if __name__ == "__main__":
    main()
