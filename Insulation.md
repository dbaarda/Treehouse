#Insulation

Insulation is all about heat energy capture/transfer via mechanisms;

* conduction - transfer of heat through materials via contact.
* convection - transfer of heat through airflow.
* radiation - transfer of heat across "transparent" gaps as emitted/absorbed
radiation.
* storage - heat energy stored in materials exposed to a high temperature that will be
released when exposed to a lower temperature.

##Conduction

Note K is degrees kelvin, which has the same scale as degrees Celcius, but a
different zero offset. So K and C can be used interchangably here. I just use
the word "degrees".

K-value (also lambda) - thermal conductivity of a meterial in W/m.K. This is
how many Watts of heat energy pass through per m^2 of surface, per heat
gradient in degrees per meter of depth. (W/m^2) / (K/m) = W/m.K. A steeper
heat-gradient (bigger temp difference and/or thinner layer) means more energy
gets through. High values mean more heat conducted through.

U-value (sometimes also called C-value. Sometimes C-value is for insulation
material, but U-value is for a whole system) - thermal conductivity of an assembly
or insulation layer in W/m^2.K. This is how many watts of heat energy pass
through per m^2 of surface per degree of temperature difference between inside
and outside. For a sheet of insulation, U is the K value divided by the
thickness in meters; (W/m.K) / m = W/m^2.K. For complicated assemblies with
multiple layers/frames/etc the U value is typically the combined/average over
the whole window+frame area. High values = more heat through.

R-value - thermal resistance in m^2.K/W. The square meters of surface area per
watt of thermal heat that gets through per degree temperature difference.
(m^2) / (W/K) = m^2.K/W. Alternatively, the temperature difference maintained
per watt passing through each square meter; (K) / (W/m^2) = m^2.K/W. R values
for insulation are typically calculated by dividing the thickness by the K
value. High values = less heat through. Note the R values of each layer can be
added together for the total R value.

L-value - sometimes used for the insulation thickness in m.

U = 1 / R = K / L

Example K-values.

Mineral wool: 0.03 - 0.04 W/mK
polypropylene 0.22 W/m·K 
polycarbonate 0.22 W/m.K
Expanded polystyrene: 0.03 - 0.04 W/mK
Extruded polystyrene: 0.02 - 0.03 W/mK
Polyurethane foam: 0.02 - 0.03 W/mK
Foilboard: 0.0366 W/mK
Cellulose fibre: 0.04 - 0.05 W/mK
Hardwood: 0.10-0.21
SoftWood: 0.08-0.17 W/mK
pine: 0.12 W/mK
MDF: 0.05-0.14  W/mK (for 250-800kg/m^3, most MDF sheets are 800kg/m^2)
Air at 0C: 0.024 W/mK
Red Brick: 0.6 W/mK
Glass: 0.8 W/mK
Steel: 50.2 W/mK
Iron: 79.5
Aluminium: 205.0
Concrete: 0.8
Water at 20C: 0.6

https://www.engineeringtoolbox.com/conductive-heat-transfer-d_428.html

Heat transferred due to conduction is;

q = U * A * dT

## Convection

https://www.engineeringtoolbox.com/convective-heat-transfer-d_430.html

heat transfer due to convection is;

q = hc * A * dT

Note this is the same as heat conduction where hc is the U value for
convection. The aprox hc value as a function of air velocity is;

hc = 12.12 - 1.16*v + 11.6*sqrt(v) # From ??? replaced with below
hc = 10.45 - v + 10*sqrt(v) # from https://www.engineeringtoolbox.com/convective-heat-transfer-d_430.html 

Note for still air v=0.0m/s this gives U=10.45W/m^2.K or R=1/10.45=0.0957,
which is about the same as conduction through 2->2.5mm of air without
convection. This is less insulation than quoted for indoor air R=0.12 which
was presumably for still air, but it is more insulation than outdoor air
R=0.04 which would include wind. However, the above formula is described as
"an empirical equation and can be used for velocities 2 to 20 m/s".  Any
induced convection currents would be way less than 2m/s so the above formula
is probably not useful.

Airgap R values,and possibly those indoor/outdoor air R values, are for a
mixture of radiation, conduction, and convection. The conductivity of air
depends on temperature and pressure, but at atmospheric pressure it's between
0.024-0.027W/m.K for 0-40C, or around 0.026W/m.K at 25C. 

https://www.engineeringtoolbox.com/air-properties-viscosity-conductivity-heat-capacity-d_1509.html

Thermal convection in airgaps means that gaps larger than 30mm provide no
additional insulation. Increased conduction distance is overcome by the
induced convection. Note that 30mm is also the practical limit for unfoiled
gaps with e=0.9 because heat transmission from radiation starts to dominate.
For radiation the distance doesn't matter, so even an infinite e=0.9 gap or
vacuume is U=5.43 or R=0.184.

Induced convection currents definitely do make a difference giving different
horiz/up/down R values. The following quoted R0.22 for "unventilated
non-reflective airspace" in a roof exceeds R0.18 for radiation@25C e=0.9,
which suggest convection might even transfer some heat back up, effectively
exceeding the performance of a vacuume in resisting heat flow down? Or are R
numbers just generally very fuzzy?

https://www.abcb.gov.au/sites/default/files/resources/2022/UTNCC-Thermal-bridging-case-study-example-03.pdf

For vertical surfaces I wonder if you can think of it in terms of a "boundary
layer" of still air with the temperature gradient and pure conduction across
it. The more "wind" the thinner the "boundary layer". An air-gap has two
boundary layers for the inner and outer layer, giving better than
outside/inside R values?


## Radiation

The amount that a surface absorbs and emits radiant heat is its "emittance".
Foil is low-emittance (e=0.05), anti-glare foil is medium emittance of e=0.4.
For white plastic e=0.84. All other surfaces considered to have e=0.9. A
"black body" would be e=1.0, absorbing and radiating 100% radiant heat. Note
that a surface's ability to absorb heat matches its ability to radiate it,
which is why the best heatsinks are black, and also explains why foil works
equally well on either side of a cavity. More detailed emissivity constants
are at;

https://www.engineeringtoolbox.com/emissivity-coefficients-d_447.html
https://www.thermoworks.com/emissivity-table/

The formula for heat radiated from a hot body to a colder space is

  q = e*Sigma*(Th^4 - Tc^44)*Ah                                    

where

  q = heat radiated in W.
  e = surface emissivity 0.0-1.0
  Sigma = = 5.6703e-8 (W/m^2.K^4) - TheStefan-Boltzmann Constant
  Th = hot body absolute temperature (K)
  Tc = cold surroundings absolute temperature (K)
  Ah = area of the hot object  (m2)

https://www.engineeringtoolbox.com/radiation-heat-transfer-d_431.html

Notice this is T^4, so it's not a simple linear eqn with dT. However, for the
small 0degC->50degC range it doesn't vary too much so can kind of be
considered constant, but I think some foil systems use different typical
winter vs typical summer temperatures to give different in/out R values for
even vertical foil+airgap configurations.

The U value is higher for higher temperatures, which might explain why
Foilboard has a different in/out or summer/winter R values for vertical-cavity
walls. In summer temps in the void would be higher, giving the void higher
radiation U values. So the void is less effective insulation during summer.

U for different e at different temps are;

e    10C   20C   25C   30C   40C
---- ----- ----- ----- ----- -----
1.00 5.17  5.73  6.03  6.34  6.99
0.90 4.65  5.16  5.43  5.71  6.29
0.85 4.39  4.87  5.13  5.39  5.94
0.10 0.517 0.573 0.603 0.634 0.699
0.05 0.258 0.287 0.302 0.317 0.349

Note that this would be for a pure vacuume. In practice there is also
conductivity and convection happening, so the R values will be lower than
that. You can add the radiation U value to the conduction/convection U value
to get the overall U value.

### Foils

Note foil insulation works by reflecting radiant heat, not resisting
conduction. So technically, foil doesn't have any R value. Any R ratings for
foil insulation are normally calculated by measuring the "total system R
value" of it's performance in a wall with cavity etc.

https://www.smartrate.com.au/media/articles/demystifying-air-gaps

https://www.continuousinsulation.org/sites/default/files/designpptairspacervalue.pdf

### Air gaps

Still air conduction/convection resistance increases as the gap increases up
to about 30mm, after which it remains nearly constant, so wider gaps don't
help. With increased venting convection becomes the dominant factor. Because
of buancy effects air gaps are given different Rhz/Rup/Rdn values. Sometimes
you also see different Rin/Rout values which account for different
summer/winter temperature radiance U values. The R value of an air gap depends
on emittance of the surfaces on either side. Low emittance surfaces (foil)
give high R-values.

https://help.iesve.com/ve2021/table_15_thermal_resistances_of_air_gaps.htm

An air gap with no foil is about R0.16. With foil is about R0.6? Note the
Foilboard calculation earlier has R0.71 for airgaps with foil. It seems it
doesn't matter what side of the gap the foil is on; foil both reflects
radiation back across the gap, and resists emitting radiation into the gap?
Would foil on both sides be even better?

So insulation can also perform differently resisting heat transfer
up/down/sideways due to convection in cavities, through material, etc,
resulting in higher resistance to heat going down compared to up. This is why
you get different "heat-flow-in" vs "heat-flow-out" R values, and you get
higher R values for roofs "in" and floors "out".

## Heat Sources

### Solar Radiation

Solar Heat Gain Coefficient (SHGC) - percentage of solar radiation hitting a
window/skylight/roof-sheet that ends up inside as thermal energy (heat)
inside. This includes transmitted radiation and absorbed and transferred in as
heat. 100% means all solar radiation turns into inside heat, 0% means none
does. For windows includes not just the glass, but the whole window frame.

single-glazed uncoated = 0.71
single glazed, grey = 0.53
double glazed, uncoated clear/clear = 0.61
double glazed, clear low-e (0.2) on surface 3 = 0.57
double glazed, clear low-e (0.1) on surface 2/ clear = 0.45

Shading Coefficient (SC) - older measure, does not consider frame, only glass
portion. ratio of heat compared to 1/8" single-glazed glass. Does take into
account exterior shading.

Note a "Peak sun hour" has 1000W/m^2 of solar radiation used for standard
solar panel rating. Solar panels are about 20% efficient so give about
200W/m^2 during a peak sun hour.

The "solar constant" has it at 1370W/m^2, though other sources have it as
1360W/m^2. One says 1380W/m^2 above the atmosphere, but about 1000W/m^2 "at
our latitude at the surface".

### Human Heat emmissions

Humans also release heat, which varies depending on activity;

https://help.iesve.com/ve2021/table_10_sensible_and_latent_gains_from_people.htm

Measured as both Sensible heat (80->190W), which is heat that directly raises
the temperature, and Latent heat (25->275W) which doesn't raise the
temperature, but raises the humidity (sweat), storing the heat energy in water
vapor which will be emitted when the vapor condenses.

Note that the combined Sensible+Latent heat energy generated by a 2m^2 surface
area human is max 465W or 232.5W/m^2, compared to 1000W/m^2 for solar radiation!

An idle human is just over 100W.

### Electric Heaters

Typical electric heaters emit about 1000W, but thermostats can down-regulate
this to the amount needed to maintain the desired temperature.

### Heat Pumps

Air conditioners can pump heat in or out, transfering more heat than they
consume, with a Coefficient of Performance (COP, heat output/power input) of
around 3->5 dependent on inside/outside temperature difference.

https://en.wikipedia.org/wiki/Coefficient_of_performance

Aircon units typically quote their cooling/heating capacity in W they can
removed/add, and their power usage. For a typical COP=4 heating efficiency
will be about 1/4 the heating capacity. It seems cooling is often a bit more
efficient with around COP=5, so they eat cooling capacity/4 power. Typical
sizes are 2.6kW-8.8kW of cooling;

https://www.kogan.com/au/buy/hyundai-88kw-inverter-smart-split-system-air-conditioner-reverse-cycle-hyundai/

### Suntuf

https://polycarbonate.com.au/domestic-product/suntuf/

For all U=5.8W/m^2.K which means they add R=1/5.8=0.17 insulation against
conducted heat. Note at only 0.8mm thick that suggests polycarbonate has
K=U*L=5.8*0.0008=0.00464W/m.K which is super insulating! However, other
sources quote polycarbonate as K=0.23W/m.K so it should be
U=K/L=0.23/0.0008=287.5W/m^2.K and R=1/U=1/287.5=0.0035. This suggests the
quoted U value must be including the corrigation air-gap effects... note an
air gap with no foil is about R0.16, so that probably explains it.

For SHGC I don't understand how heat transmission% can be higher than SHGC for
some suntuf colours. Is this what % of light shines through in the non-visible
spectrum, and light transmission is in the visible spectrum?

For Smooth Cream SHGC=0.331 and Sand Dune SHGC=0.305. This means 30~33% of
that 1kW/m^2 of peak sun will enter the roof cavity. The foilboard will
reflect 95% of that back, but I'm guessing that the polycarbonate will work
the same way in the other direction, so 70~67% of the reflected light will be
reflected back in, and out again etc. If you iterate this you end up with
<5% of the radiant heat getting in (4.54% cream, 4.49% sanddune), or about
45W/m^2.

The good news is the roof will be shaded by the tree, so it's likely to be
less than half that, or maybe 20W/m^2, or 180W total for 9m^2 of roof.

At 20W/m^2 heat going into the cavity, if it was sealed, you would then have
heat conducting out the polycarbonate to outside, and heat conducting in
through the foilboard to the house. Is simply treating it as 20W/m^2 heat
passing through the total R of the roof a good enough approximation? Probably
not.

### Foilboard

https://insulationessentials.com.au/wp-content/uploads/2022/10/Foilboard-Tech-Data-Sheet-JAN-22.pdf

Foilboard 15mm is quoted as 0.41 for just the board in this;

https://www.betaboard.com.au/content/userfiles/files/products/FOILBOARD/FOILBOARD%20THERMAL%20PERFORMANCE%20R%20Calc%20BV%2070mm%20Frame.pdf

Which suggests K= L/R = 0.015/0.41 = 0.0366.

10mm foilboard in theory has R = L/K = 0.01/0.0366 = 0.27 but together with
the foil and air-gap on both sides and the rest of the roof it bumps up to
1.4-5.6. For 20mm is 0.02/0.0366 = 0.55, but Skillion Roof Green 20 total is
R2.2 out, R3.1 in.

https://www.foilboard.com.au/wp-content/uploads/2023/04/FOILBOARD-FINAL-2023-APRIL-DIGITAL.pdf

This has the raw R values not including radiant foil effects, and shows it as
R0.13 per 5mm thickness.

outdoor air        0.04
outside foil gap   0.71
foamboard 10mm     0.26
inside foil gap    0.71
indoor air         0.12

total = R1.84, of which only 0.26 is the board. But without the foilboard and
just a cavity you have 0.04+0.16+0.12 = 0.32, so foilboard adds R1.52, of which
R1.28 is just due to the double-sided foil&air-gaps.

### Corflute

Corflute is polypropyline cardboard. Polypropyline has K=0.22W/mK d=0.9g/cm^3.
Tunnelcore 5mm has d=0.18g/cm^2, which means the cross section is only
0.18/0.9=0.2 or 20% solid. This suggests a 0.35mm thickness wall.

Calculations in the following spreadsheet give the corflute R values of;

https://docs.google.com/spreadsheets/d/17m0OmeC3FWWI7BKIIBJTtw7Bf-GojhWo89HRaAEcK3U/edit?gid=1464144108#gid=1464144108

tunnelcore 3mm R0.052
tunnelcore 5mm R0.075
tunnelcore 8mm R0.095

###Modeling

3x3x2m room,

floor=9m^2
roof=9m^2
walls=24m^2
total=42m^2

10degree diff, all R=2.0 = 5W/m^2 so 42*5=210W to maintain a 10deg temp
difference, or 420W for 20deg.

On hot days the floor is going to be a problem with heat rising through it.

layer               R
-------------
outside air       0.04
suntuf roof       0.17 (does this include the air-gap? Should this be 0.0035
for just the sheet?)
air gap (dn)      1.2?
foilboard 20mm    0.52
air gap (dn)      1.2?
ceiling sheet     0.003/0.14=0.02
indoor air        0.12
total 3.28

##Thermal bridging effects.

Wood is more heat conductive than air, so heat will conduct through timber
past air gaps. This can even cause condensation on inside walls over the
studs, discolouring paint.

Metal nails and screws are also very conductive, at least 500x as conducitive
as wood, 

Pine with K=0.12 has R=L/K = 0.01/0.12 = R0.083 per 10mm, or R0.58 across the
70mm wall stud thickness. Foilboard is R0.26 per 10mm, and air-gaps with foil
are R0.71 horizontally. So 10mm foilboard in a wall void is 0.71+0.26+0.71=R1.68 compared
to R0.58 for the stud. This means, assuming energy flow through both is the
same, 1.1 degrees difference per W/m^2 energy flow, so for an overall R=2.0
void with a temp difference of 10degrees (5W/m^2), the wall in front of a stud
will be 5.5 degrees colder than the wall in front of a void. In practice it
could is lower because the energy flow through the low-resistance stud
will be higher than through the void and it equalizes with the inside
air.

For a wall over a foilboard void upto the indoor surface and including the indoor
air barrier it is;

Rv=2.0
Uv=1/2.0=0.5
Rvw=Rv+Rai=2.0+0.12 = 2.12
Uvw=1/Rvw=1/2.12 = 0.472

For a wall over a stud upto the indoor surface;

Rs=0.9
Us=1/Rs=1/0.9 = 1.1
Rsw=Rs+Rai=0.9+0.12 = 1.02
Usw=1/Rsw=1/1.02 = 0.980

For dt=10deg between inside and outside, heat through void wall and stud wall;

dt=10deg
Evw=Uvw*dt=0.472*10=4.72W/m^2
Esw=Usw*dt=0.980*10=9.80W/m^2

So temp difference at the inside wall surface is;

dtv = Rv*Evw = 2.0*4.72=9.44deg
dts = Rs*Esw = 0.9*9.80=8.82deg
dtvs = dtv-dts=9.44-8.82=0.62deg
Esw/Evw=9.80/4.72 = 2.08x

So the wall over a stud will be 0.62 degrees colder than the wall over a
foilboard void per 10deg of difference between the inside and outside air, and
heat flow through the stud is more than 2x/m^2 of the flow through the void.

If studs make up 3.5cm/45cm~=8% of the wall, the overall wall is;

Utw=0.92*Uvw+0.08*Usw=0.92*0.472+0.08*0.980 = 0.513W/m^2.K
Rtw=1/U=1/0.51264 = 1.95m^2.K/W
Etw=Utw*dt=0.513*10 = 5.13W/m^2

Rvw-Rtw=2.12-1.95 = 0.17
Etw-Evw=5.13-4.72 = 0.41W/m^2
Etw/Evw=5.13/4.72 = 1.09x

So the studs lower the overall wall by R0.17, and increase the energy flow by
0.41W/m^2 or 9%.

Now lets put the foilboard over the outside studs, and add a 10mm wooden cavity
batten over the studs. The void wall has the same R/U values, but the stud becomes;

R's=Rs+Rf10+Lb/Kwood=0.9+0.26+0.01/0.12=1.24
U's=1/1.24=0.806

R'sw=R's+Rai=1.24+0.12=1.36
U'sw=1/1.36=0.735

E'sw=U'vw*dt=0.735*10=7.35W/m^2

dt's=R's*E'sw=1.24*7.35=9.11deg
dt'vs=dtv-dt's=9.44-9.11=0.33deg
E'sw/Evw=7.35/4.72 = 1.56x

U'tw=0.92*Uvw+0.8*U'sw=0.92*0.472+0.08*0.735=0.493
R'tw=1/0.493=2.03
E'tw=U'tw*dt=0.493*10 = 4.93W/m^2

Rvw-R'tw=2.12-2.03 = 0.09
E'tw-Evw=4.93-4.72 = 0.21W/m^2
E'tw/Evw=4.93/4.72 = 1.04x  

Comparing with/without thermal break;

R's-Rs=1.24-0.9 = 0.32
R'tw-Rtw=2.03-1.95 = 0.08
E'tw-Etw=4.93-5.13 = -0.20W/m^2
E'tw/Etw=4.93/5.13 = 0.94x
dt'vs-dtvs=0.33-0.62 = -0.29deg
dt'vs/dtvs=0.33/0.62 = 0.53x

So the foilboard thermal break improves wall by R0.08 and reduces the wall
temp difference over studs by 0.29deg per 10deg of temp difference, or nearly
halves the temp difference. It also reduces the energy flow by 0.2W/m^s, or 6%.

Using an insulating cavity batten increases the stud by a further R0.17, which
should add about half as much again.

### Thermal bridging through fastners.

The effect of metal nails/screws might not be trivial. For 10G screws are
4.8mm diameter and 50~65mm long. That's an area of about 18mm^2, and with 4
per 2m stud they make up (4*18)/(35*2000) = 0.1% of the stud area and go 71%
of the depth. However, with K values of 50.2/0.12 = 418x pine they do this to
the stud U value;

Lr=Ls-Lf

Rfr=Rf+Rr=Lf/Ksteel+Lr/Kwood = (Lf*Kwood + Lr*Ksteel)/(Ksteel*Kwood)
Ufr=1/Rfr=(Ksteel*Kwood)/(Lf*Kwood + Lr*Ksteel)
   = (50.2*0.12)/(0.05*0.12+0.02*50.2) = 5.96
Us=Ls/Kwood = 0.07/0.12 = 0.58
Rs=1/Us=1/0.58=1.72
Ufs=0.001*Ufr + 0.999*Us
   = 0.001*5.96 + 0.999*0.58 = 0.585
Rfs=1/Ufs= 1/0.585 = 1.71

Rfs-Rs=1.71-1.72 = -0.01
Rfs/Rs=1.71/1.72 = 0.994

So the screws lower the stud by R0.01 or 0.6%, a trivial amount. The Lr gap in
the stud without faster significantly saves this, acting as a thermal break.
If the faster goes all the way through, we get;

Ufr=Ksteel/Lf=717.1
Ufs=0.001*Ufr + 0.999*Us = 0.001*717.1 + 0.999*0.58 = 1.30
RfS=1/Ufs=0.769

Rfs-Rs=0.769-1.72 = -0.95
Rfs/Rs=0.769/1.72 = 0.45

So 2xG10/m screws all the way through a 35x70mm stud drops the stud by R0.95
or 55%!

This thermal bridging effect also affects fastners through foilboard, and
probably even more!

I've seen online talk of using plastic nails to avoid this problem. I'm not
sure if they were joking, does such a thing exist?
