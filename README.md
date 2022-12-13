# Solent Trip Management System [STMS]

**1. You need to run the HomePage.py to start the system**

**2. Interpreter need to be set to python 3.8 before starting the system.**

**3. Administrator Username: root and Password: 123456**

**4. You can create other users from Administrator**

#Problem Scenario#
------------------

Solent Trips is based in Southampton, UK and organises both national and international trips. Each trip is organised as a group trip with group sizes varying anywhere between a small family to a large party. Each trip may involve visiting one or more locations, includes transport and may involve staying in accommodation where the trip lasts more than a day. Currently, Solent Trips employs a paper-based system where passengers make appointments directly with staff, arrange their trip and make payments with a receipt manually issued as evidence of payment. Payments may be made in one go or in multiple instalments but must be paid in full before the start of the trip. This process results in tremendous paperwork for staff, ineffective validation of payment and process and serious complaints from travellers regarding inefficiency. As Solent Trips grow over time, there is a significant need for an electronic system for the management of these activities. 

*Following features in the development of the system:*
------------------------------------------------------

**Trip**

A trip has a name, a start date and consists of multiple travellers and trip legs. Each trip will always have a contact, the trip coordinator, who is in-charge and manages the trip. Depending on the number of travellers, the trip may also have multiple support staff to assist with the trip. In terms of duration, a trip may be a one-day trip, a weekend (Friday evening to Sunday evening) trip, or a fortnight trip.

**Traveller**

A traveller has a name, an address, date of birth, and an emergency contact. Each traveller will have at least one valid form of government id (a passport, driving license, national identity card, etc.) with details of the id stored in the system.

**Trip Leg**

A trip leg is a part of the trip and will have a starting location, a destination, a transport provider, and a mode of transport. The starting location and destination can be a place to stay (e.g., a hotel, bed & breakfast, etc.), a point of interest (such as a museum, historical site, etc.) or a transfer point (e.g., an airport, a ferry port, etc.). The mode of transport will be a plane, ferry, coach, or taxi.

**System Users**

Users are the system actors who will carry out different activities using the system. The system users are considered in three categories as follows:

*Trip Coordinator*

A trip coordinator is associated with a trip and will be able to carry out basic functionalities in the system. These include:
i. Create, view, and update the passengers for a trip.
ii. Create, view, and update the trips legs for a trip.
iii. Generate an itinerary for the trip.
iv. Take payments on behalf of passengers and generate a receipt
v. Print invoices and receipts for any payments that have been made.

*Trip Manager*

A trip manager will be able to complete all user tasks as stated above and, additionally, the following:
i. Create, view, update, and delete trip coordinators
ii. Create, view, update and delete trips.
iii. Generate a total invoice for any trip they manage.

*Administrator*

An administrator will be able to complete all the tasks as stated above as well as the following:
i. create, view, update and delete trip managers.
ii. view, update and delete trip invoices and payments.
iii. view the total invoice and payment receipt for all trips within the system.

**This project is maintained in the below GitHub Repository as Private. If you need any further details you can contact the owner through 5sivas01@solent.ac.uk**

https://github.com/sivaseran/trip-managment-system
