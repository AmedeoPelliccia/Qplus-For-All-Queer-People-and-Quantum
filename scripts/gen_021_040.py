#!/usr/bin/env python3
"""
gen_021_040.py
Generate the full S1000D-CSDB scaffold for DMC-AMPEL360E-EWTW-021-040
(Heating Subsystem, ATA 21-40).
"""

import os
import pathlib

BASE = pathlib.Path(
    "/home/runner/work/Qplus-For-All-Queer-People-and-Quantum"
    "/Qplus-For-All-Queer-People-and-Quantum"
    "/Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family"
    "/Q+ATLANTIDE_impact-study/000-099_ATLAS-impact-analysis"
    "/020-029_Sistemas-Core-de-Aeronave"
    "/021-Conditioning-and-Pressurization/S1000D-CSDB/DMC"
    "/DMC-AMPEL360E-EWTW-021-040"
)

# ── Lookup tables ─────────────────────────────────────────────────────────────

FOLDER_USE = {
    "040_descriptive": "system description / descriptive data module",
    "100_operation": "operation / operating procedures",
    "200_servicing": "servicing procedures",
    "300_examinations-tests-and-checks": "inspection, examinations, tests and checks",
    "400_fault-reports-and-isolation-procedures": "fault reporting and fault isolation procedures",
    "500_disconnect-remove-and-disassembly-procedures": "disconnect, remove and disassembly procedures",
    "600_repairs-and-locally-make-procedures-and-data": "repairs and locally make procedures and data",
    "700_assemble-install-and-connect-procedures": "assemble, install and connect procedures",
    "800_package-handling-storage-and-transportation": "package, handling, storage and transportation procedures",
    "940_provisioning-data": "provisioning data",
    "941_illustrated-parts-data": "illustrated parts data",
    "C00_computer-systems-software-and-data": "computer systems, software and data",
}

INFO_NAME_LOWER = {
    "040": "the system description",
    "100": "operational information",
    "200": "servicing procedures",
    "300": "inspection and examination data",
    "310": "operational check procedures",
    "320": "functional test procedures",
    "400": "fault reporting procedures",
    "420": "fault isolation procedures",
    "520": "remove procedures",
    "600": "repair data",
    "720": "install procedures",
    "800": "packaging procedures",
    "940": "provisioning data",
    "941": "illustrated parts data",
    "C00": "software configuration and control data",
}

# ── Component definitions ─────────────────────────────────────────────────────

def _file(code, name, fn_suffix):
    """Helper: build a file-entry dict."""
    return {"infoCode": code, "infoName": name, "fn_suffix": fn_suffix}


COMPONENTS = [
    {
        "assyCode": "00A",
        "disassyCode": "00",
        "folderName": "00A_Heating-Subsystem-General",
        "techName": "Heating Subsystem General",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heating-Subsystem-General-Description"),
            ]},
            {"folderName": "100_operation", "files": [
                _file("100", "Operation", "Heating-Subsystem-General-Operation"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "General Inspection", "Heating-Subsystem-General-Inspection"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heating-Subsystem-Fault-Reporting"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heating-Subsystem-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "01A",
        "disassyCode": "01",
        "folderName": "01A_Electric-Air-Heater",
        "techName": "Electric Air Heater",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Electric-Air-Heater-Description"),
            ]},
            {"folderName": "200_servicing", "files": [
                _file("200", "Servicing", "Electric-Air-Heater-Servicing"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Electric-Air-Heater-Inspection"),
                _file("310", "Operational Check", "Electric-Air-Heater-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Electric-Air-Heater-Fault-Reporting"),
                _file("420", "Fault Isolation", "Electric-Air-Heater-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Electric-Air-Heater-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Electric-Air-Heater-Install-Procedure"),
            ]},
            {"folderName": "800_package-handling-storage-and-transportation", "files": [
                _file("800", "Packaging Procedure", "Electric-Air-Heater-Packaging-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Electric-Air-Heater-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Electric-Air-Heater-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "02A",
        "disassyCode": "02",
        "folderName": "02A_Cabin-Zone-Heater",
        "techName": "Cabin Zone Heater",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Cabin-Zone-Heater-Description"),
            ]},
            {"folderName": "200_servicing", "files": [
                _file("200", "Servicing", "Cabin-Zone-Heater-Servicing"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Cabin-Zone-Heater-Inspection"),
                _file("310", "Operational Check", "Cabin-Zone-Heater-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Cabin-Zone-Heater-Fault-Reporting"),
                _file("420", "Fault Isolation", "Cabin-Zone-Heater-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Cabin-Zone-Heater-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Cabin-Zone-Heater-Install-Procedure"),
            ]},
            {"folderName": "800_package-handling-storage-and-transportation", "files": [
                _file("800", "Packaging Procedure", "Cabin-Zone-Heater-Packaging-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Cabin-Zone-Heater-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Cabin-Zone-Heater-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "03A",
        "disassyCode": "03",
        "folderName": "03A_Flight-Deck-Heater",
        "techName": "Flight Deck Heater",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Flight-Deck-Heater-Description"),
            ]},
            {"folderName": "200_servicing", "files": [
                _file("200", "Servicing", "Flight-Deck-Heater-Servicing"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Flight-Deck-Heater-Inspection"),
                _file("310", "Operational Check", "Flight-Deck-Heater-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Flight-Deck-Heater-Fault-Reporting"),
                _file("420", "Fault Isolation", "Flight-Deck-Heater-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Flight-Deck-Heater-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Flight-Deck-Heater-Install-Procedure"),
            ]},
            {"folderName": "800_package-handling-storage-and-transportation", "files": [
                _file("800", "Packaging Procedure", "Flight-Deck-Heater-Packaging-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Flight-Deck-Heater-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Flight-Deck-Heater-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "04A",
        "disassyCode": "04",
        "folderName": "04A_Floor-and-Sidewall-Heating-Elements",
        "techName": "Floor and Sidewall Heating Elements",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Floor-and-Sidewall-Heating-Elements-Description"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Floor-and-Sidewall-Heating-Elements-Inspection"),
                _file("310", "Operational Check", "Floor-and-Sidewall-Heating-Elements-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Floor-and-Sidewall-Heating-Elements-Fault-Reporting"),
                _file("420", "Fault Isolation", "Floor-and-Sidewall-Heating-Elements-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Floor-and-Sidewall-Heating-Elements-Remove-Procedure"),
            ]},
            {"folderName": "600_repairs-and-locally-make-procedures-and-data", "files": [
                _file("600", "Repair Data", "Floor-and-Sidewall-Heating-Elements-Repair-Data"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Floor-and-Sidewall-Heating-Elements-Install-Procedure"),
            ]},
            {"folderName": "800_package-handling-storage-and-transportation", "files": [
                _file("800", "Packaging Procedure", "Floor-and-Sidewall-Heating-Elements-Packaging-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Floor-and-Sidewall-Heating-Elements-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Floor-and-Sidewall-Heating-Elements-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "05A",
        "disassyCode": "05",
        "folderName": "05A_Duct-Heater-and-Air-Temperature-Rise-Unit",
        "techName": "Duct Heater and Air Temperature Rise Unit",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Duct-Heater-and-Air-Temperature-Rise-Unit-Description"),
            ]},
            {"folderName": "200_servicing", "files": [
                _file("200", "Servicing", "Duct-Heater-and-Air-Temperature-Rise-Unit-Servicing"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Duct-Heater-and-Air-Temperature-Rise-Unit-Inspection"),
                _file("310", "Operational Check", "Duct-Heater-and-Air-Temperature-Rise-Unit-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Duct-Heater-and-Air-Temperature-Rise-Unit-Fault-Reporting"),
                _file("420", "Fault Isolation", "Duct-Heater-and-Air-Temperature-Rise-Unit-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Duct-Heater-and-Air-Temperature-Rise-Unit-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Duct-Heater-and-Air-Temperature-Rise-Unit-Install-Procedure"),
            ]},
            {"folderName": "800_package-handling-storage-and-transportation", "files": [
                _file("800", "Packaging Procedure", "Duct-Heater-and-Air-Temperature-Rise-Unit-Packaging-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Duct-Heater-and-Air-Temperature-Rise-Unit-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Duct-Heater-and-Air-Temperature-Rise-Unit-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "06A",
        "disassyCode": "06",
        "folderName": "06A_Windshield-and-Window-Demist-Heating-Interface",
        "techName": "Windshield and Window Demist Heating Interface",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Windshield-and-Window-Demist-Heating-Interface-Description"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Windshield-and-Window-Demist-Heating-Interface-Inspection"),
                _file("310", "Operational Check", "Windshield-and-Window-Demist-Heating-Interface-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Windshield-and-Window-Demist-Heating-Interface-Fault-Reporting"),
                _file("420", "Fault Isolation", "Windshield-and-Window-Demist-Heating-Interface-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Windshield-and-Window-Demist-Heating-Interface-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Windshield-and-Window-Demist-Heating-Interface-Install-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Windshield-and-Window-Demist-Heating-Interface-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Windshield-and-Window-Demist-Heating-Interface-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "07A",
        "disassyCode": "07",
        "folderName": "07A_Heater-Power-Controller",
        "techName": "Heater Power Controller",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heater-Power-Controller-Description"),
            ]},
            {"folderName": "100_operation", "files": [
                _file("100", "Operation", "Heater-Power-Controller-Operation"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heater-Power-Controller-Inspection"),
                _file("320", "Functional Test", "Heater-Power-Controller-Functional-Test"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heater-Power-Controller-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heater-Power-Controller-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Heater-Power-Controller-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heater-Power-Controller-Install-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Heater-Power-Controller-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heater-Power-Controller-Illustrated-Parts-Data"),
            ]},
            {"folderName": "C00_computer-systems-software-and-data", "files": [
                _file("C00", "Software Data", "Heater-Power-Controller-Software-Data"),
            ]},
        ],
    },
    {
        "assyCode": "08A",
        "disassyCode": "08",
        "folderName": "08A_Heater-Temperature-Sensors-and-Limiters",
        "techName": "Heater Temperature Sensors and Limiters",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heater-Temperature-Sensors-and-Limiters-Description"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heater-Temperature-Sensors-and-Limiters-Inspection"),
                _file("310", "Operational Check", "Heater-Temperature-Sensors-and-Limiters-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heater-Temperature-Sensors-and-Limiters-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heater-Temperature-Sensors-and-Limiters-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Heater-Temperature-Sensors-and-Limiters-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heater-Temperature-Sensors-and-Limiters-Install-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Heater-Temperature-Sensors-and-Limiters-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heater-Temperature-Sensors-and-Limiters-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "09A",
        "disassyCode": "09",
        "folderName": "09A_Heating-Control-Valves-and-Airflow-Interfaces",
        "techName": "Heating Control Valves and Airflow Interfaces",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heating-Control-Valves-and-Airflow-Interfaces-Description"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heating-Control-Valves-and-Airflow-Interfaces-Inspection"),
                _file("310", "Operational Check", "Heating-Control-Valves-and-Airflow-Interfaces-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heating-Control-Valves-and-Airflow-Interfaces-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heating-Control-Valves-and-Airflow-Interfaces-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Heating-Control-Valves-and-Airflow-Interfaces-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heating-Control-Valves-and-Airflow-Interfaces-Install-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Heating-Control-Valves-and-Airflow-Interfaces-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heating-Control-Valves-and-Airflow-Interfaces-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "10A",
        "disassyCode": "10",
        "folderName": "10A_Heating-Overtemperature-Protection",
        "techName": "Heating Overtemperature Protection",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heating-Overtemperature-Protection-Description"),
            ]},
            {"folderName": "100_operation", "files": [
                _file("100", "Operation", "Heating-Overtemperature-Protection-Operation"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heating-Overtemperature-Protection-Inspection"),
                _file("320", "Functional Test", "Heating-Overtemperature-Protection-Functional-Test"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heating-Overtemperature-Protection-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heating-Overtemperature-Protection-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Heating-Overtemperature-Protection-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heating-Overtemperature-Protection-Install-Procedure"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heating-Overtemperature-Protection-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "11A",
        "disassyCode": "11",
        "folderName": "11A_Heating-Monitoring-BITE-and-Diagnostics",
        "techName": "Heating Monitoring BITE and Diagnostics",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heating-Monitoring-BITE-and-Diagnostics-Description"),
            ]},
            {"folderName": "100_operation", "files": [
                _file("100", "Operation", "Heating-Monitoring-BITE-and-Diagnostics-Operation"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heating-Monitoring-BITE-and-Diagnostics-Inspection"),
                _file("320", "Functional Test", "Heating-Monitoring-BITE-and-Diagnostics-Functional-Test"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heating-Monitoring-BITE-and-Diagnostics-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heating-Monitoring-BITE-and-Diagnostics-Fault-Isolation"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heating-Monitoring-BITE-and-Diagnostics-Install-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Heating-Monitoring-BITE-and-Diagnostics-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heating-Monitoring-BITE-and-Diagnostics-Illustrated-Parts-Data"),
            ]},
            {"folderName": "C00_computer-systems-software-and-data", "files": [
                _file("C00", "Software Data", "Heating-Monitoring-BITE-and-Diagnostics-Software-Data"),
            ]},
        ],
    },
    {
        "assyCode": "12A",
        "disassyCode": "12",
        "folderName": "12A_Heating-Wiring-Connectors-and-Bonding-Interfaces",
        "techName": "Heating Wiring Connectors and Bonding Interfaces",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Description"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Inspection"),
                _file("310", "Operational Check", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Install-Procedure"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heating-Wiring-Connectors-and-Bonding-Interfaces-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "13A",
        "disassyCode": "13",
        "folderName": "13A_Heating-Maintenance-Access-and-Mounting-Interfaces",
        "techName": "Heating Maintenance Access and Mounting Interfaces",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heating-Maintenance-Access-and-Mounting-Interfaces-Description"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heating-Maintenance-Access-and-Mounting-Interfaces-Inspection"),
                _file("310", "Operational Check", "Heating-Maintenance-Access-and-Mounting-Interfaces-Operational-Check"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heating-Maintenance-Access-and-Mounting-Interfaces-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heating-Maintenance-Access-and-Mounting-Interfaces-Fault-Isolation"),
            ]},
            {"folderName": "500_disconnect-remove-and-disassembly-procedures", "files": [
                _file("520", "Remove Procedure", "Heating-Maintenance-Access-and-Mounting-Interfaces-Remove-Procedure"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heating-Maintenance-Access-and-Mounting-Interfaces-Install-Procedure"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heating-Maintenance-Access-and-Mounting-Interfaces-Illustrated-Parts-Data"),
            ]},
        ],
    },
    {
        "assyCode": "14A",
        "disassyCode": "14",
        "folderName": "14A_Heating-Software-Configuration-and-Control-Data",
        "techName": "Heating Software Configuration and Control Data",
        "infoFolders": [
            {"folderName": "040_descriptive", "files": [
                _file("040", "Description", "Heating-Software-Configuration-and-Control-Data-Description"),
            ]},
            {"folderName": "100_operation", "files": [
                _file("100", "Operation", "Heating-Software-Configuration-and-Control-Data-Operation"),
            ]},
            {"folderName": "300_examinations-tests-and-checks", "files": [
                _file("300", "Inspection", "Heating-Software-Configuration-and-Control-Data-Inspection"),
                _file("320", "Functional Test", "Heating-Software-Configuration-and-Control-Data-Functional-Test"),
            ]},
            {"folderName": "400_fault-reports-and-isolation-procedures", "files": [
                _file("400", "Fault Reporting", "Heating-Software-Configuration-and-Control-Data-Fault-Reporting"),
                _file("420", "Fault Isolation", "Heating-Software-Configuration-and-Control-Data-Fault-Isolation"),
            ]},
            {"folderName": "700_assemble-install-and-connect-procedures", "files": [
                _file("720", "Install Procedure", "Heating-Software-Configuration-and-Control-Data-Install-Procedure"),
            ]},
            {"folderName": "940_provisioning-data", "files": [
                _file("940", "Provisioning Data", "Heating-Software-Configuration-and-Control-Data-Provisioning-Data"),
            ]},
            {"folderName": "941_illustrated-parts-data", "files": [
                _file("941", "Illustrated Parts Data", "Heating-Software-Configuration-and-Control-Data-Illustrated-Parts-Data"),
            ]},
            {"folderName": "C00_computer-systems-software-and-data", "files": [
                _file("C00", "Software Data", "Heating-Software-Configuration-and-Control-Data-Software-Data"),
            ]},
        ],
    },
]

# ── Content generators ────────────────────────────────────────────────────────

def xml_content(assyCode, disassyCode, infoCode, techName, infoName):
    infoNameLower = INFO_NAME_LOWER.get(infoCode, infoName.lower())
    dmc = f"DMC-AMPEL360E-EWTW-021-040-{assyCode}-{infoCode}A-D"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!-- ============================================================
     S1000D Data Module
     DMC: {dmc}
     Title: {techName} \u2014 {infoName}
     Programme: AMPEL360e Wide Tube-and-Wing Family (eWTW)
     ATLAS Node: 021-040 / 021-040-{assyCode} / ATA 21-40
     Info Code: {infoCode}A \u2014 {infoName}
     Status: draft / programme-controlled-placeholder
     Issue: 001-00 | Date: 2026-05-10
     Note: Programme-controlled scaffold placeholder pending BREX/DMRL freeze.
     ============================================================ -->
<dmodule xmlns:xlink="http://www.w3.org/1999/xlink">

  <identAndStatusSection>
    <dmAddress>
      <dmIdent>
        <dmCode modelIdentCode="AMPEL360E"
                systemDiffCode="EWTW"
                systemCode="021"
                subSystemCode="0"
                subSubSystemCode="40"
                assyCode="{assyCode}"
                disassyCode="{disassyCode}"
                disassyCodeVariant="A"
                infoCode="{infoCode}"
                infoCodeVariant="A"
                itemLocationCode="D"/>
        <language languageIsoCode="en" countryIsoCode="001"/>
        <issueInfo issueNumber="001" inWork="00"/>
      </dmIdent>
      <dmAddressItems>
        <issueDate year="2026" month="05" day="10"/>
        <dmTitle>
          <techName>{techName}</techName>
          <infoName>{infoName}</infoName>
        </dmTitle>
      </dmAddressItems>
    </dmAddress>

    <dmStatus issueType="new">
      <security securityClassification="01"/>
      <responsiblePartnerCompany enterpriseCode="AMPEL360E">
        <enterpriseName>AMPEL360 / Q+ Programme</enterpriseName>
      </responsiblePartnerCompany>
      <originator enterpriseCode="AMPEL360E">
        <enterpriseName>AMPEL360 / Q+ Programme</enterpriseName>
      </originator>
      <applic>
        <displayText>
          <simplePara>AMPEL360e Wide Tube-and-Wing Family (eWTW) \u2014 All variants</simplePara>
        </displayText>
      </applic>
      <brexDmRef>
        <dmRef>
          <dmRefIdent>
            <dmCode modelIdentCode="AMPEL360E"
                    systemDiffCode="EWTW"
                    systemCode="000"
                    subSystemCode="0"
                    subSubSystemCode="00"
                    assyCode="00A"
                    disassyCode="00"
                    disassyCodeVariant="A"
                    infoCode="022"
                    infoCodeVariant="A"
                    itemLocationCode="D"/>
          </dmRefIdent>
        </dmRef>
      </brexDmRef>
      <qualityAssurance>
        <unverified/>
      </qualityAssurance>
      <remarks>
        <simplePara>Programme-controlled placeholder. infoCode {infoCode}A subject to BREX/SNS/DMRL freeze. Not for operational use.</simplePara>
      </remarks>
    </dmStatus>
  </identAndStatusSection>

  <content>
    <description>
      <levelledPara id="desc-{infoCode}-001">
        <title>{infoName}</title>
        <para>This data module provides {infoNameLower} for the <emphasis emphasisType="em01">{techName}</emphasis> of the AMPEL360e eWTW Heating Subsystem (ATLAS 021-040 / ATA 21-40). Content is a programme-controlled scaffold placeholder pending BREX/DMRL freeze.</para>
      </levelledPara>
    </description>
  </content>

</dmodule>
"""


def infocode_folder_readme(assyCode, folderName, baseInfoCode, xmlFilenames):
    folderUse = FOLDER_USE.get(folderName, folderName)
    dmc_group = f"DMC-AMPEL360E-EWTW-021-040-{assyCode}"
    file_lines = "\n".join(f"- `{fn}`" for fn in xmlFilenames)
    return f"""---
document_id: DMC-AMPEL360E-EWTW-021-040-{assyCode}-{baseInfoCode}-README
title: "Info-Code Folder \u2014 {folderName}"
dmc_group: "{dmc_group}"
folder_use: "{folderUse}"
status: "programme-controlled-scaffold-placeholder"
brex_note: "infoCode admissibility, schema selection and naming constraints shall be frozen in project BREX and DMRL before controlled release."
created: 2026-05-10
---

# {folderName}

**DMC Group:** `{dmc_group}`  
**Folder use:** {folderUse}

## Files in this folder

{file_lines}

---

> Programme-controlled scaffold placeholder. Not for operational use. Subject to BREX/SNS/DMRL freeze.
"""


def component_readme(comp):
    assyCode = comp["assyCode"]
    folderName = comp["folderName"]
    techName = comp["techName"]
    infoFolders = comp["infoFolders"]
    dmc_group = f"DMC-AMPEL360E-EWTW-021-040-{assyCode}"

    # Flatten all files for the Recommended DM Set table
    all_files = []
    for fd in infoFolders:
        for f in fd["files"]:
            filename = f"DMC-AMPEL360E-EWTW-021-040-{assyCode}-{f['infoCode']}A-D_{f['fn_suffix']}.xml"
            all_files.append({"infoCode": f["infoCode"], "infoName": f["infoName"],
                               "filename": filename})

    # Info-Code Folder Index table
    folder_rows = []
    for fd in infoFolders:
        codes = ", ".join(f["infoCode"] for f in fd["files"])
        use = FOLDER_USE.get(fd["folderName"], fd["folderName"])
        folder_rows.append(f"| `{fd['folderName']}/` | {codes} | {use} |")
    folder_table = "\n".join(folder_rows)

    # Recommended DM Set table
    dm_rows = []
    for f in all_files:
        dm_rows.append(f"| {f['infoCode']} | {techName} \u2014 {f['infoName']} | `{f['filename']}` |")
    dm_table = "\n".join(dm_rows)

    return f"""---
document_id: {dmc_group}-GROUP-README
title: "DMC Group \u2014 {dmc_group}"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 \u2014 Conditioning and Pressurization"
sub_system: "021-040 \u2014 Heating Subsystem"
component: "{techName}"
sns: "021-040-{assyCode}"
ata_reference: "ATA 21-40"
model_ident_code: "AMPEL360E"
system_diff_code: "EWTW"
system_code: "021"
sub_system_code: "0"
sub_sub_system_code: "40"
assy_code: "{assyCode}"
item_location_code: "D"
status: "programme-controlled-scaffold-placeholder"
created: 2026-05-10
classification: "open-technical-scaffold"
primary_q_division: "Q-DATAGOV"
support_q_divisions:
  - "Q-AIR"
  - "Q-MECHANICS"
  - "Q-INDUSTRY"
lifecycle_phase:
  - "LC03"
  - "LC05"
  - "LC06"
  - "LC11"
  - "LC12"
review_status: "to-be-reviewed-by-system-expert"
---

# DMC Group: {dmc_group}

## Identification

**Programme:** AMPEL360e Wide Tube-and-Wing Family  
**Short code:** eWTW  
**System:** 021 \u2014 Conditioning and Pressurization  
**Sub-system:** 021-040 \u2014 Heating Subsystem  
**Component:** {techName}  
**SNS node:** 021-040-{assyCode}  
**ATA reference:** ATA 21-40  
**DMC group:** {dmc_group}  

## Purpose

This DMC group contains the S1000D/CSDB scaffold for the **021-040 / {assyCode} {techName}** node of the AMPEL360e eWTW Heating Subsystem.

The group covers design description, operation, maintenance, inspection, fault isolation, removal/installation, and illustrated parts data for the {techName} within the ATA 21-40 Heating Subsystem.

## System Scope

The {techName} is a constituent of the AMPEL360e eWTW Heating Subsystem (ATA 21-40). Its main functions include:

- provide or support the heating function for the assigned zone or element;
- interface with heating power supply, control, and overtemperature protection architecture;
- support maintenance, inspection, removal, and reinstallation activities;
- provide fault detection, isolation, and BITE interfaces where applicable.

## Info-Code Folder Index

| Folder | Info Code(s) | Use |
|---|---|---|
{folder_table}

## Recommended Data Module Set

| Info code | Data module purpose | Suggested filename |
|---:|---|---|
{dm_table}

## Technical Boundaries

### Included

- all mechanical and electrical elements of the {techName} assembly;
- electrical power supply and control interfaces within the component boundary;
- thermal and airflow interfaces within the heating subsystem boundary;
- mounting hardware, fasteners, and structural attachment interfaces;
- sensor, limiter, and BITE interfaces associated with this component;
- wiring, connectors, and bonding interfaces within the component boundary;
- maintenance access panels and mounting interfaces directly associated with this component.

### Excluded

- elements assigned to adjacent heating subsystem components;
- cabin temperature-control algorithms outside the component control boundary;
- pressurization-control architecture (ATA 21-30);
- anti-ice and de-ice systems (ATA 30);
- supplier-controlled proprietary design data unless released to the CSDB baseline;
- ground support equipment not permanently installed on the aircraft.

## Traceability

| Trace item | Value |
|---|---|
| ATLAS branch | `000-099_ATLAS/020-029_Sistemas-Core-de-Aeronave/021-Conditioning-and-Pressurization` |
| Programme path | `Programmes_example/090_AMPEL360e-Wide-Tube-and-Wing-Family` |
| S1000D group path | `S1000D-CSDB/DMC/DMC-AMPEL360E-EWTW-021-040/{folderName}` |
| Parent DMC group | `DMC-AMPEL360E-EWTW-021-040-00A` |
| SNS | `021-040-{assyCode}` |
| ATA reference | `ATA 21-40` |
| DMC prefix | `{dmc_group}` |
| Primary lifecycle use | LC05 Detailed Design / LC06 Verification Planning / LC11 Operation / LC12 Maintenance Support |

## Review and Governance

> Programme-controlled scaffold. Content is subject to BREX, SNS, applicability, DMRL, and CCB freeze before controlled release.

> **To be reviewed by system expert.**
"""


def toplevel_readme():
    rows = []
    for c in COMPONENTS:
        rows.append(
            f"| `{c['folderName']}/` | DMC-AMPEL360E-EWTW-021-040-{c['assyCode']} | {c['techName']} |"
        )
    table = "\n".join(rows)
    return f"""---
document_id: DMC-AMPEL360E-EWTW-021-040-TOP-README
title: "DMC Group \u2014 DMC-AMPEL360E-EWTW-021-040 Heating Subsystem"
programme: "AMPEL360e Wide Tube-and-Wing Family"
short_code: "eWTW"
system: "021 \u2014 Conditioning and Pressurization"
sub_system: "021-040 \u2014 Heating Subsystem"
atlas_node: "021-040"
ata_alignment: "ATA 21-40"
status: "programme-controlled-scaffold-placeholder"
created: 2026-05-10
---

# DMC Group: DMC-AMPEL360E-EWTW-021-040 \u2014 Heating Subsystem

**System:** 021 \u2014 Conditioning and Pressurization  
**Sub-system:** 021-040 \u2014 Heating Subsystem  
**ATA alignment:** ATA 21-40

## Component Folder Index

| Folder | DMC Group Root | Component |
|---|---|---|
{table}

---

> Programme-controlled scaffold. All component folders and Data Modules subject to BREX/SNS/DMRL freeze by programme CCB before controlled release.
"""


# ── Main generation ───────────────────────────────────────────────────────────

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  CREATED  {path.relative_to(BASE)}")


def main():
    print(f"Generating scaffold under:\n  {BASE}\n")
    file_count = 0

    # Top-level README
    write(BASE / "README.md", toplevel_readme())
    file_count += 1

    for comp in COMPONENTS:
        assyCode = comp["assyCode"]
        disassyCode = comp["disassyCode"]
        compFolder = BASE / comp["folderName"]
        techName = comp["techName"]

        # Component README
        write(compFolder / "README.md", component_readme(comp))
        file_count += 1

        for fd in comp["infoFolders"]:
            folderName = fd["folderName"]
            icFolder = compFolder / folderName

            # Collect XML filenames for this info-code folder
            xml_filenames = []
            for f in fd["files"]:
                fn = f"DMC-AMPEL360E-EWTW-021-040-{assyCode}-{f['infoCode']}A-D_{f['fn_suffix']}.xml"
                xml_filenames.append(fn)

                # Write XML file
                xml = xml_content(assyCode, disassyCode, f["infoCode"], techName, f["infoName"])
                write(icFolder / fn, xml)
                file_count += 1

            # Base info code for folder README doc-id: first code in this folder
            baseInfoCode = fd["files"][0]["infoCode"]

            # Info-code folder README
            write(
                icFolder / "README.md",
                infocode_folder_readme(assyCode, folderName, baseInfoCode, xml_filenames),
            )
            file_count += 1

    print(f"\nDone. {file_count} files created.")


if __name__ == "__main__":
    main()
