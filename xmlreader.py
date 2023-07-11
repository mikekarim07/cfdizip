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
En esta versión modificada, hemos agregado el parámetro accept_multiple_files=True al llamar a st.file_uploader para permitir la carga de varios archivos ZIP a la vez. Dentro del bucle for que recorre uploaded_files, se procesa cada archivo ZIP de la misma manera que en la versión anterior.

Recuerda personalizar la función extract_xml_data para adaptarla a la estructura de tus archivos XML y extraer los datos que necesitas. También puedes realizar cualquier otra operación con los datos extraídos dentro del bucle for, como almacenarlos en una lista, guardarlos en una base de datos, mostrarlos en una tabla, etc.

Asegúrate de tener instaladas las bibliotecas necesarias, como Streamlit y xml.etree.ElementTree. Puedes usar el comando pip install streamlit para instalar Streamlit si aún no lo tienes en tu entorno Python.





User

2 / 2

ayudame a adaptar el siguiente codigo para que haga lo siguiente:
1) Upload zip files
2) uncompress zip files
3) leer y extraer datos de los xml de acuerdo a las funciones parse_xml4, parse_xml33, parse_xmlcomp33, parse_xmlcomp40, parse_xml32
4) organizar la data en dataframes

codigo:
import os
import time
import pandas as pd
import xml.etree.ElementTree as ET
import streamlit as st
from streamlit_option_menu import option_menu
import io
import base64
import zipfile

st.set_page_config(
    page_title="CDFI Lector archivos xml - webappmmmmmmmm",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

def parse_xml4(xml_file):
    #code

def parse_xml33(xml_file):
    #code

def parse_xmlcomp33(xml_file):
    #code

def parse_xmlcomp40(xml_file):
    #code

def parse_xml32(xml_file):
    #code


def main():
    uploaded_files = st.file_uploader('Cargar archivos ZIP', accept_multiple_files=True, type='zip')
    rfc_busqueda = st.text_input('Ingresa el RFC de la sociedad que deseas filtrar:', max_chars=13)

    if st.button('Procesar') and uploaded_files:
        xml_files = []

     for uploaded_file in uploaded_files:
        if uploaded_file:
            with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
                xml_files = [file for file in zip_ref.namelist() if file.endswith('.xml')]

                for xml_file in xml_files:
                    xml_content = zip_ref.read(xml_file)
                    data = extract_xml_data(xml_content)

        total_archivos = len(xml_files)
        st.info(f'Total de archivos cargados: {total_archivos}')

        start_time = time.time()

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

        for xml_path in xml_files:
            try:
                xml_data_parse_xml4 = parse_xml4(xml_path)
                data_parse_xml4.append(xml_data_parse_xml4)
            except Exception as e:
                xml_files_not_processed_parse_xml4.append(xml_path)

            try:
                xml_data_parse_xml33 = parse_xml33(xml_path)
                data_parse_xml33.append(xml_data_parse_xml33)
            except Exception as e:
                xml_files_not_processed_parse_xml33.append(xml_path)

            try:
                xml_data_parse_xml32 = parse_xml32(xml_path)
                data_parse_xml32.append(xml_data_parse_xml32)
            except Exception as e:
                xml_files_not_processed_parse_xml32.append(xml_path)

            try:
                xml_data_parse_xmlcomp33 = parse_xmlcomp33(xml_path)
                data_parse_xmlcomp33.append(xml_data_parse_xmlcomp33)
            except Exception as e:
                xml_files_not_processed_parse_xmlcomp33.append(xml_path)

            try:
                xml_data_parse_xmlcomp40 = parse_xmlcomp40(xml_path)
                data_parse_xmlcomp40.append(xml_data_parse_xmlcomp40)
            except Exception as e:
                xml_files_not_processed_parse_xmlcomp40.append(xml_path)

        end_time = time.time()
        processing_time = end_time - start_time
        processing_time_formatted = "{:.4f}".format(processing_time)
        st.info(f'Se encontraron un total de {total_archivos} archivos, los cuales fueron procesados en un tiempo total de: {processing_time_formatted} segundos')

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

ChatGPT
Aquí tienes el código modificado para realizar las tareas que mencionaste:

python
Copy code
import os
import time
import pandas as pd
import xml.etree.ElementTree as ET
import streamlit as st
import io
import base64
import zipfile

def parse_xml4(xml_file):
    # Código para parsear el XML y extraer los datos según la función parse_xml4
    # Personaliza esta función según tus necesidades
    # Devuelve un diccionario con los datos extraídos del XML
    pass

def parse_xml33(xml_file):
    # Código para parsear el XML y extraer los datos según la función parse_xml33
    # Personaliza esta función según tus necesidades
    # Devuelve un diccionario con los datos extraídos del XML
    pass

def parse_xmlcomp33(xml_file):
    # Código para parsear el XML y extraer los datos según la función parse_xmlcomp33
    # Personaliza esta función según tus necesidades
    # Devuelve un diccionario con los datos extraídos del XML
    pass

def parse_xmlcomp40(xml_file):
    # Código para parsear el XML y extraer los datos según la función parse_xmlcomp40
    # Personaliza esta función según tus necesidades
    # Devuelve un diccionario con los datos extraídos del XML
    pass

def parse_xml32(xml_file):
    # Código para parsear el XML y extraer los datos según la función parse_xml32
    # Personaliza esta función según tus necesidades
    # Devuelve un diccionario con los datos extraídos del XML
    pass

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
