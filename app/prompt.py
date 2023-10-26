completion_prompt = '''
Common Context - A shipper lists their shipments in spot market for carriers to bid on. As a carrier I am participating in bidding on a shipment that is posted on a bid board by the shipper. The shipment has all the requirements listed in English and I need to classify the requirements in order to calculate the cost of transporting this shipment. While I can calculate the cost for fuel, there are some incurred costs like lumper fees, team drivers and driver assist that I need to add to know the total cost.
Loading Context - A truck sometimes needs to be loaded or unloaded at the facility after reaching the facility called live loading or live pickup or live load. When this is not needed it is called drop shipment or drop trailer load or drop trailer as the truck's tracktor or the engine only needs to pickup or drop the trailer from or to a facility. When the truck needs to be loaded at a facility using labor, the cost for this labor is the incurred cost or lumper fees. When this labor is unavailable the truck's driver is required to assist in loading or unloading the truck which is called Driver Assist or DA. Loading may require that the truck have tailgate or doors at the back to be opened after docking at the facility. It may require pallet jack or electric pallet jack or fork lift or a truck with lift gate to load or unload. If driver is required to operate any of these tools then they may required to be trained, qualified and certified for it.
Team Driver Context - If a shipment has urgency or needs to be shipped as soon as possible, then it may be termed as hot or priority shipment. Every commercial vehicle or truck is required to follow regulations like HoS or Hours of Service from the FMCSA. This means that no driver can drive more than 10 hours in a day. Shipments that are urgent and would take more than 10 hours to ship require the use of two drivers driving the truck alternatively as a team. The freight industry terms this as Team Drivers or Team. As average speed limit of US highways is 55 miles per hour, a shipment farther than 400 miles may require team drivers while an urgent shipment under 400 miles does not require team drivers.
Following things we need to identify
Lumper(defined by Loading Context) - Does this shipment need lumpers to load or unload the truck?
Driver Assist(defined by Loading Context) - Does this shipment need driver to assist in loading, unloading, sorting  or workin or segregating this truck's load?
Team Drivers(defined by Team Driver Context) - Does this shipment need team drivers to complete the shipment?
Example -
--------
Comment: "UNFI requires all pallets to be broken down to their standards upon delivery. Driver can do this or a lumper service can be used."
output: "{'Lumper': True, 'DriverAssist': True, 'TeamDriver': False}"
-------

'''
MESSGAE = [
    {
      "role": "system",
      "content": completion_prompt
    },
    {
      "role": "user",
      "content": "Driver Help Unload."
    },
    {
      "role": "assistant",
      "content": "{'Lumper': False, 'DriverAssist': True, 'TeamDriver': False}"
    },
    {
      "role": "user",
      "content": "PLEASE SHIP WITH 5415912095es lumper charges."
    },
    {
      "role": "assistant",
      "content": "{'Lumper': True, 'DriverAssist': False, 'TeamDriver': False}"
    },
    {
      "role": "user",
      "content": "TEAMS IF NEEDED TO DELIVER ON TIME."
    },
    {
      "role": "assistant",
      "content": "{'Lumper': False, 'DriverAssist': False, 'TeamDriver': True}"
    },
    {
      "role": "user",
      "content": "Floor load only."
    },
    {
      "role": "assistant",
      "content": "{'Lumper': False, 'DriverAssist': False, 'TeamDriver': False}"
    }
]
