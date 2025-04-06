# Gungor:
- The electrical grid has been aging and more has been demanded of it for 100 yearswith no updates
- Proposes using a "smart grid" which'll improve efficiency, reliabilty, and safety through automated controls and modern communications
### This paper details:
1. smart grid communication technologies and their advangtages/disadvantaves
2. security, reliability, robustness, availability, scalability and quality-of-service requirements
3. the standardization activities

## 1. smart grid communication technologies and their advangtages/disadvantaves
- Wireless means needs batteries but wired solutions means you gotta deal with that esky wire
- There are 2 types of information to flow
    1. Sensor/electrical appliances to smart meters
    2. smart meters and the utility data centers
- From here, the author provides the pros and cons to different communication methods:

| Technology | Spectrum               | Data Rate       | Coverage Range         | Applications                    | Limitations                       |
|------------|------------------------|-----------------|------------------------|----------------------------------|-----------------------------------|
| GSM        | 900-1800 MHz            | Up to 14.4 Kbps | 1-10 km                | AMI, Demand Response, HAN       | Low data rates                    |
| GPRS       | 900-1800 MHz            | Up to 170 kbps  | 1-10 km                | AMI, Demand Response, HAN       | Low data rates                    |
| 3G         | 1.92-1.98 GHz, 2.11-2.17 GHz (licensed) | 384 Kbps-2 Mbps  | 1-10 km                | AMI, Demand Response, HAN       | Costly spectrum fees             |
| WiMAX      | 2.5 GHz, 3.5 GHz, 5.8 GHz | Up to 75 Mbps   | 10-50 km (LOS), 1-5 km (NLOS) | AMI, Demand Response           | Not widespread                    |
| PLC        | 1-30 MHz                | 2-3 Mbps        | 1-3 km                 | AMI, Fraud Detection            | Harsh, noisy channel environment  |
| ZigBee     | 2.4 GHz, 868-915 MHz    | 250 Kbps        | 30-50 m                | AMI, HAN                        | Low data rate, short range        |

- GSM = Cellular Communication. It's the 2G phone tech.
- PLC = Powerline Communication. Hard because the enviornment it's communicating through (powerlines) are noisy
- DSLs = Digital Subscriber Lines (The old internet)
- WiMAX = WiMAX (Worldwide Interoperability for Microwave Access) is a wireless communication technology designed to provide high-speed internet and data services over long distances. It operates based on IEEE 802.16 standards and is often used for broadband access in areas where traditional wired infrastructure is difficult or expensive to deploy.
- ZigBee = A short range, low data method that is good for residential

## 2. System REliability, Robustness, and availability
- All it says is that it basically needs to be reliable, secure, robust, available, and have a high Quality of Service

## 3. Smart grid standards
- Goes into detail about the standards available. Table summary below:

| **Type/Name of Standards**         | **Details**                                                                 | **Application**                        |
|------------------------------------|-----------------------------------------------------------------------------|----------------------------------------|
| IEC 61970 and IEC 61969           | Providing Common Information Model (CIM): IEC 61970 works in transmission, IEC 61969 in distribution | Energy management systems              |
| IEC 61850                          | Flexible, future-proofing, open standard, communication between devices in transmission, distribution, and substation automation | Substation Automation                  |
| IEC 60870-6 /TASE.2                | Data exchange between utility control centers, utilities, power pools, regional control centers | Inter-control center communications    |
| IEC 62351 Parts 1-8               | Defining cyber security for the communication protocols                      | Information Security Systems           |
| IEEE P2030                         | A Guide for smart grid interoperability of energy technology and IT operations with EPS | Customer-side applications             |
| IEEE P1901                         | High-speed power line communications                                          | In-home multimedia, utility, smart grid applications |
| ITU-T G.9955 and G.9956            | Physical layer and data link layer specifications                            | Distribution Automation, AMI           |
| OpenADR                            | Dynamic pricing, Demand Response                                              | Price Responsive and Load Control     |
| BACnet                             | Scalable system communications at customer side                              | Building automation                    |
| HomePlug                           | Powerline technology to connect smart appliances to HAN                      | HAN                                    |
| HomePlug Green PHY                 | Low-power, cost-optimized power line networking for smart grid applications   | HAN                                    |
| U-SNAP                             | Communication protocols to connect HAN devices to smart meters               | HAN                                    |
| ISA100.11a                         | Open standard for wireless systems                                            | Industrial Automation                  |
| SAE J2293                          | Standard for electrical energy transfer from utility to EVs                   | Electric Vehicle Supply Equipment      |
| ANSI C12.22                        | Data network communications, C12.19 tables are transported                   | AMI                                    |
| ANSI C12.18                        | Data structures transported via infrared optical port                        | AMI                                    |
| ANSI C12.19                        | Flexible metering model for common data structures and industry "vocabulary" for meter data communications | AMI                                    |
| Z-Wave                             | Alternative to ZigBee, handles interference with 802.11/b/g                   | HAN                                    |
| M-Bus                              | European standard for remotely reading all kinds of utility meters           | AMI                                    |
| PRIME                              | Open, global standard for multi-vendor interoperability                      | AMI                                    |
| G3-PLC                             | Providing interoperability, cyber security, and robustness                   | AMI                                    |
| SAE J2836                          | Supporting use cases for plug-in electric vehicle communication              | Electric Vehicle                       |
| SAE J2847                          | Supports communication messages between PEVs and grid components             | Electric Vehicle                       |

# Falco:
- A case study of using the below to save energy and cut costs
    1. Fault dedection and diagnosis of equipment
    2. Alarm Management to prioritize building systems
    3. Energy management through tracking and optimization
- It's put together by accenture
- With less than 10% of annual energy cost (1.2 months) with a payback period of less than 2 years.

- This can be replicated by:
    1. Identifying, collecting, and aggregating relevant data
    2. Employing industry-leading analytics to identify savings
    3. Present results in a consumable and actionable form
    4. Centralize monitoring operations
    5. Engaging the organization - Put the dashboards out where people can see them. They'll start being mindful
    6. Avoid disruptive changes - existing systems don't need to be replaced but new systems can be added to make it better