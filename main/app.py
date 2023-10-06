import streamlit as st
import requests
import pandas as pd

def generate_card(product_id, product_name, summary, img_link, product_link):
    card_html = f"""
    <style>

    .card-product {{
      overflow: hidden;
      background: #262730;
      border: 1px solid #1F2633;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      display: flex;
      align-items: flex-start;
      margin: 5px;
      transition: background-color 0.3s, transform 0.3s;
    }}

    .card-product:hover {{
      background: #1F2633;
      transform: translateY(-5px);
    }}

    .card-link {{
      text-decoration: none;
    }}

    .card-product img {{
      height: 150px;
      width: 150px;
      object-fit: cover;
      margin: 10px;
    }}

    .card-product h2 {{
      font-size: 18px;
      margin: 0;
      margin-top: 10px;
      padding: 0;
      color: #E3EEF8;
    }}

    .card-product p {{
      font-size: 11px;
      line-height: 1.4;
      margin-top: 5px;
      color: #D1D7E8;
    }}

    .card-product .card-product-infos {{
      padding: 0px;
      align-items:top;
      color: White;
    }}


    .card-product .brief {{
      font-size: 12px;
      margin-top: 10px;
      padding: 0px;
      color: #D7DEF5;
    }}

    .card-product .product-summary {{
      font-size: 11px;
      margin-top: 0px;
      margin: 0px;
      padding: 0px;
      color: #C3CEE0;
    }}

    </style>
    <a href="{product_link}" class="card-link">
      <div class="card-product">
        <img src="{img_link}" alt="{product_name}" />
        <div class="card-product-infos">
          <h2 class="product-title">{product_name}</h2>
          <p class="brief"><b>Summary of reviews</b></p>
          <p class="product-summary">{summary}...</p>
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

        amazon_api_url = 'https://amazon-reviews-api-hezmcck7ba-nw.a.run.app/predict'
        response = requests.get(amazon_api_url, params=params)

        if response.status_code == 200:
            prediction = response.json()
            message = prediction['message']
            data = prediction.get("data", None)

            if data:
                if isinstance(data, str):
                    if len(data.strip()) > 0:
                        st.write("Thank you for your feedback.")
                else:
                    df_results = pd.DataFrame({
                        'Product ID': list(data.get('product_id', {}).values()),
                        'Product Name': list(data.get('product_name', {}).values()),
                        'Summary': list(data.get('summary', {}).values()),
                        'img_link': list(data.get('img_link', {}).values()),
                        'product_link': list(data.get('product_link', {}).values()),
                    })

                    if not df_results.empty:
                        st.write(message)
                        for index, row in df_results.iterrows():
                            card_html = generate_card(row['Product ID'], row['Product Name'], row['Summary'], row["img_link"], row["product_link"])
                            st.write(card_html, unsafe_allow_html=True)
                    if len(data) == 1:
                        st.write(message)

            else:
                st.write(message)

        else:
            st.write("Request Failed with Status Code:", response.status_code)
