import streamlit as st
import requests
import pandas as pd
#def generate_card(product_id, product_name, summary, image_url, link_url):
# {image_url} {link_url}
def generate_card(product_id, product_name, summary):
    card_html = f"""
    <style>
    .card-product {{
      overflow: hidden;
      height: 192px;
      background: #262730;
      box-shadow: 0 0 15px rgba(0,0,0,0.2);
      display: flex;
      align-items: top;
      margin: 5px;
    }}
    .card-product img {{
      height: 100%;
      width: 190px;
      object-fit: cover;
    }}
    .card-product h2 {{
      font-size: 16px;
      font-weight: bold;
      margin: 0;
      color: White;
      opacity: 0.76;
    }}
    .card-product p {{
      font-size: 12px;
      line-height: 1.4;
      opacity: .7;
      margin-bottom: 0;
      margin-top: 8px;
    }}
    .card-product .card-product-infos {{
      padding: 16px;
      color: White;
      background-color: #262730
    }}

    .body {{
        background-color: #262730
    }}

    </style>
    <a href="https://www.google.com">
      <div class="card-product">
        <img src="https://m.media-amazon.com/images/W/WEBP_402378-T1/images/I/51UsScvHQNL._SX300_SY300_QL70_FMwebp_.jpg" />
        <div class="card-product-infos">
          <h2>{product_name}</h2>
          <p>{summary}</p>
        </div>
      </div>
    </a>
    """
    return card_html




# Streamlit UI elements
st.title("Alternative Product Recommendations")
product = st.selectbox(f'Product Category', ('Choose your product category', '3DGlasses',	'Adapters&Multi-Outlets',	'Adapters',
                                             'AirFryers',	'AirPurifiers&Ionizers',	'AutomobileChargers',	'AVReceivers&Amplifiers',
                                             'BackgroundSupports',	'Basic',	'BasicCases',	'BasicMobiles',	'BatteryChargers',
                                             'Bedstand&DeskMounts',	'BluetoothAdapters',	'BluetoothSpeakers',	'BottledInk',
                                             'CableConnectionProtectors',	'Caddies',	'CameraPrivacyCovers',	'CanisterVacuums',
                                             'Cases',	'CeilingFans',	'Choppers',	'CleaningKits',	'CoffeePresses',	'ColdPressJuicers',
                                             'ColouredPaper',	'ColouringPens&Markers',	'CompleteTripodUnits',	'CompositionNotebooks',
                                             'Condenser',	'CoolingPads',	'CordManagement',	'Cradles',	'DÃ©cor',	'DataCards&Dongles',
                                             'DigitalBathroomScales',	'DigitalKitchenScales',	'DigitalScales',	'DisposableBatteries',
                                             'DomeCameras',	'DripCoffeeMachines',	'DryIrons',	'DustCovers',	'DVICables',	'Earpads',
                                             'EggBoilers',	'ElectricGrinders',	'ElectricHeaters',	'ElectricKettles',	'EspressoMachines',
                                             'EthernetCables',	'ExhaustFans',	'ExternalHardDisks',	'ExternalMemoryCardReaders',
                                             'ExternalSolidStateDrives',	'FanHeaters',	'FanParts&Accessories',	'Film',	'Financial&Business',
                                             'FountainPens',	'Gamepads',	'GamingKeyboards',	'GamingMice',	'GelInkRollerballPens',
                                             'GeneralPurposeBatteries&BatteryChargers',	'GraphicTablets',	'HalogenHeaters',	'HandBlenders',
                                             'HandheldBags',	'HandheldVacuums',	'HandlebarMounts',	'HandMixers',	'HardDiskBags',	'HDMICables',
                                             'Headsets',	'HeatConvectors',	'HEPAAirPurifiers',	'Humidifiers',	'ImmersionRods',	'InductionCooktop',
                                             'In-Ear',	'InkjetInkCartridges',	'InkjetInkRefills&Kits',	'InkjetPrinters',	'InstantWaterHeaters',
                                             'InternalSolidStateDrives',	'JuicerMixerGrinders',	'Juicers',	'Kettle&ToasterSets',	'Keyboard&MouseSets',
                                             'Keyboards',	'Lamps',	'Lapdesks',	'LaptopAccessories',	'LaptopChargers&PowerSupplies',
                                             'LaptopSleeves&Slipcases',	'LaundryBags',	'LaundryBaskets',	'LintShavers',	'LiquidInkRollerballPens',
                                             'Macro&RinglightFlashes',	'MeasuringSpoons',	'Memory',	'Mice',	'MicroSD',	'MilkFrothers',
                                             'MiniFoodProcessors&Choppers',	'MixerGrinders',	'Monitors',	'Mounts',	'MousePads',
                                             'MultimediaSpeakerSystems',	'NetworkingDevices',	'NotebookComputerStands',
                                             'Notebooks,WritingPads&Diaries',	'Notepads&MemoBooks',	'On-Ear',	'OpticalCables',
                                             'OTGAdapters',	'OutdoorSpeakers',	'OvenToasterGrills',	'Over-Ear',	'PaintingMaterials',
                                             'Paints',	'PCHeadsets',	'PCMicrophones',	'PCSpeakers',	'PedestalFans',	'PenDrives',
                                             'Pens',	'PhoneCharms',	'Pop-upToasters',	'PowerBanks',	'PowerLANAdapters',
                                             'PressureWashers,Steam&WindowCleaners',	'Printers',	'Projectors',	'RCACables',
                                             'RechargeableBatteries',	'RemoteControls',	'Repeaters&Extenders',	'RetractableBallpointPens',
                                             'Rice&PastaCookers',	'RoboticVacuums',	'RoomHeaters',	'RotiMakers',	'Routers',
                                             'SandwichMakers',	'SATACables',	'SatelliteReceivers',	'Scientific',	'ScreenProtectors',
                                             'SecureDigitalCards',	'SelfieLights',	'SelfieSticks',	'Sewing&EmbroideryMachines',	'Shower&WallMounts',
                                             'SmallApplianceParts&Accessories',	'SmallKitchenAppliances',	'Smartphones',	'SmartTelevisions',
                                             'SmartWatches',	'SoundbarSpeakers',	'SpeakerCables',	'Split-SystemAirConditioners',	'SprayBottles',
                                             'StandardTelevisions',	'StandMixerAccessories',	'StandMixers',	'Stands',	'SteamIrons',
                                             'StickBallpointPens',	'StorageWaterHeaters',	'StovetopEspressoPots',	'StreamingClients',
                                             'StylusPens',	'SurgeProtectors',	'TableFans',	'Tabletop&TravelTripods',	'Tablets',
                                             'Tape',	'TonerCartridges',	'TowerSpeakers',	'TraditionalLaptops',	'TripodLegs',
                                             'Tripods',	'TVWall&CeilingMounts',	'UninterruptedPowerSupplies',	'USBCables',	'USBHubs',
                                             'USBtoUSBAdapters',	'VacuumSealers',	'VideoCameras',	'WaffleMakers&Irons',	'WallChargers',
                                             'WaterCartridges',	'WaterFilters&Purifiers',	'WaterPurifierAccessories',	'Webcams',	'Wet-DryVacuums',
                                             'WetGrinders',	'WireboundNotebooks',	'WirelessUSBAdapters',	'WoodenPencils',	'YogurtMakers'))
review = st.text_input("Enter your review")


if st.button('Submit'):
    if product == "Choose your product category":
        st.write("Choose a product category and try again")
    else:
        params = dict(
            product_category=product,
            text=review
        )

        amazon_api_url = 'https://final-test-hezmcck7ba-nw.a.run.app/predict'
        response = requests.get(amazon_api_url, params=params)

        if response.status_code == 200:
            prediction = response.json()
            message = prediction['message']
            if prediction["data"]:

                df_results = pd.DataFrame({
                                'Product ID': list(prediction['data']['product_id'].values()),
                                'Product Name': list(prediction['data']['product_name'].values()),
                                'Summary': list(prediction['data']['summary'].values())
                                })


                if not df_results.empty:
                    st.write(message)
                    for index, row in df_results.iterrows():
                        card_html = generate_card(row['Product ID'], row['Product Name'], row['Summary'])
                        st.write(card_html, unsafe_allow_html=True)

            else:
                st.write(message)

        else:
            st.write("Request Failed with Status Code:", response.status_code)
