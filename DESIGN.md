# *Project* DESIGN

::: contents
**Contents**
:::

## Introduction

### Identification

This is the \<Software Design Document\> for the \<Project Name\>.
\<Project Name\> is being developed according to \<SDP-DocId\>
\"Software Development Plan for the \<Project Name\>\". The requirements
for \<Project Name\> are identified in the \<SRS-DocId\> \"Software
Requirements Specification for the \<Project Name\>\".

### Document Overview

### System Overview

## Design Details

### Inspirations and Origins

### Design Philosophy

### General Architecture

#### Wall bracing

Diagonal bracing is needed for walls, floor and roof.

Turns out it's pretty much essential for ensuring your walls are true/square.
I used ratchet-straps to bring the walls square before putting on the
gavanized strapping to ensure the strapping was tight enough... there's a
limit to how much the strap tightners can do. Another tip; put the first nail
all the way through a strap-hole, tilt the nail a bit in the direction you
want to tighten it before starting to hammer it in. As it goes in it will pull
the strap tighter.

Need additional 4.5*2 + 1.8*2 = 12.6m

#### Cavity Battens

Using foilboard as the moisture barrier for both walls and roof means I'll
need cavity battens for both.

Cavity battens are to give a cavity gap between the wall
foil/moisture-barrier/sarking and the outer cladding. This gap is so moisture
that gets to, or condenses on, the barrier can drain down and to allow airflow
to help evaporation. The cavity also improves foil insulation performance with
gaps of at least 20mm recommended, but 10mm is sufficient for drainage/ventilation.

The bottom of the cavity is sealed with a perforated cavity closer that allows
drainage/airflow but blocks pests. Sometimes there is also a cavity top-vent
to give even better airflow while preventing easy water ingress.

For vertical corrigated sheet cladding an alternative cavity-closer is
flashing that protrudes past the outer edge of the cladding, leaving a small
gap for ventilation but small enought to prevent pests.

Simple cavity battens are normally rectangular profile strips installed mostly
vertically on top of the barrier and attached to the studs behind them. The
attachments are usually staggered nails, leaving the middle of the batten
clear to put the horizontal cladding attachments through (long nails or
screws), but sometimes glue or tape fixing is sufficient and the cladding
attachments through the batten to the studs becomes the primary attachment.
This vertical batten arrangement gives a clear gap for moisture to drain down.
They can also sometimes be put horizontally on top of noggings, but then there
is a minium 50mm gap on either end to allow vertical drainage/airflow and they
are mounted at a 5deg angle to drain water off them.

For mounting wall cladding vertically instead of horizontally, the attachment
points tend to be horizontally aligned, requiring the cavity battens to be
horizontal. For this castellated cavity battens are normally used. These
include castelated cutout "gaps" on both sides of the batten to allow vertical
flow/drainage past them on both the barrier side, and the cladding side. They
also include a 13|15|18 degree bevelled/sloped top side so that moisture drains
away from the barrier towards the cladding. Sometimes the bottom is also
bevelled to prevent moisture wicking back to the barrier on the bottom of the
batten. In theory a drip-cut could also help, but I've not seen that.
Standards require at least 1000mm^2/m worth of gaps past the batten, but most
castelated battens have at least 2x that much, with 20x5mm castelations
alternating on both sides.

With horizontal battens, there is often not a corresponding horizontal line of
noggings/studs to directly attach the batten to. In this case, structural
battens can be used, which are strong enough to directly attach the cladding
to without a stud directly behind the cladding attachemnt point.

There are also platic battens, that usually have corrigation-like ventilation
through them for mounting horizontally. They are typically not structural.

https://www.ventsystems.com.au/products/vb20-wall-cavity-batten/

For the walls, with vertical polycarbonate cladding we need horizontal cavity
battens. Note that the greca profile is itself already "castelated" with
16mm/2 * 1000mm = 8000mm^2/m of ventilation even if directly attached to the
foilboard. However, foil insulation will do better with an additional gap. We
can get away without castelated battens provided we either have regular 50mm
gaps and mount them on 5deg angles (a pain), or put a bevelled edge on the top
(and probably bottom) to drain towards the cladding to run down the greca
"castelation gaps". Given the castelation gaps, we can probably get away with a
smaller gap of maybe even 5mm?

For the roof, the structural roof battens that the polycabonate roofing is
attached to are run "horizontaly" perpendicular to the roof slope. This means
we cannot just put them on top of the roof foilboard membrane, but need to add
"vertical" cavity battens under them over the rafters. The roof battens add a
35mm gap between the foilboard and roof sheeting which helps insulation, and
the sheet "castelation gaps" allow "vertical" airflow over the roof batten,
but a gap is still needed for drainage flow under them. These are sometimes
called "counter-battens".

The roof cavity battens need to provide a drainage gap of at least 5mm under
the roof battens. They also need to help distribute the load from the roof battens
so that it doesn't just crush into the foilboard. This means we can't just put
square spacers under where the roof-battens attach through the foilboard to
the rafters.

We are going to need 3 walls * 4 strips * 3m + 1 wall * 3 strips * 3m + 8 rafters
* 3.6m ~= 75m of cavity battens.

I originally thought of using [Weathertex 1220 x 45 x 9.5mm Cavity
Batten](https://www.bunnings.com.au/weathertex-1220-x-45-x-9-5mm-cavity-batten_p0240107)
which work out as $2.15/m. 

Then I realized I could cut a 90x35mm MPG10 beam into 8 35x9mm cavity battens.
For a more normal batten size that would distribute the foilboard load a
little better you could cut 6 44x10mm battens, or use 90x45 for 8 45x9mm
battens. For MPG10 H3 90x35mm costing $5.95/m the battens would be ~$0.75/m or
~$1/m, and for MPG10 H3 90x45mm costing $7/m they would be $0.88/m.

Wooden battens must be at least H3 treated to protect them from rot, and cut
H3 timber needs to be re-treated on the cuts with H3 level timber
preservative. Cut into strips like this so much needs re-treating you might as
well use untreated pine (MPG10 untreated 90x35 for $4/m, or $0.50/m battens)
and treat it all afterwards, or even non-structural pine (non-structural 90x45
$3.20/m or $0.40/m).

Bunnings only has sprayon cut sealers, 300g for $19.50. There is also
brushon/soak stuff available at Pestrol Australia at 2L for $49.90. You need
0.25l per m^2, or about 70m of 45x10mm battens per 2L tin, adding $0.71/m to
the cost, bringing even the cheapest non-structural battens to $1.11/m.

* [TWA Woodcare 300g Ecoseal Tanalised Timber Treatment
(H5)](https://www.bunnings.com.au/twa-woodcare-300g-ecoseal-tanalised-timber-treatment_p0960107?region_id=117368&gad_source=1&gclid=CjwKCAjwhvi0BhA4EiwAX25ujzla-CljmYDD65BSbPG5IcUs8UdU8JuA3JwGO_e05kN-Xc1A-6f2_RoC60MQAvD_BwE&gclsrc=aw.ds)

* [Tanalised 300g Clear Enseal Timber Treatment
(H3)](https://www.bunnings.com.au/tanalised-300g-clear-enseal-timber-treatment_p0960108?store=7368&gad_source=1&gclid=CjwKCAjwhvi0BhA4EiwAX25uj-s_5gLG0J8AahA8CNyLlMayatkaLHK-nZNHTH7D-YwDq7ZjBCLpexoCwykQAvD_BwE&gclsrc=aw.ds)

* [XJ Timber Preservative 2L](https://www.pestrol.com.au/buy-online/xj-timber-preservative/?attribute_size=2L&srsltid=AfmBOopzdbFT2eSXQnVPTzUh03STFplsUIE57-Q1Rno_7CPmakWffjNU5ZA)

This makes the Weathertex battons look more appealing. Less work and no nasty
treatment costs/process. They will probably still need bevelling for the
horizontal wall battons. Not much info on what they are made of (hardwood?)
but I suspect it's a hardwood composite that will not need treating.

Other options are [permatimber 42 x 18mm DAR]
(https://www.bunnings.com.au/permatimber-42-x-18mm-2-7m-arctic-white-pvc-composite-dar_p0497592)
cut into 2 42x7.8mm battens ($5.44/2 = $2.72/m battens).

[42x11mm 5.4m H3 Treated Pine FJ DAR Primed
LOSP](https://www.bunnings.com.au/42-x-11mm-5-4m-h3-treated-pine-fj-dar-primed-losp_p0020736)
used as-is for 42x11mm battons ($4.11/m), but will also need beveling and cut
treating.

[QuickBoard 300 x 9mm 2.7m Arctic White PVC VJ Wall and Ceiling Lining Board -
2
Pack](https://www.bunnings.com.au/quickboard-300-x-9mm-2-7m-arctic-white-pvc-vj-wall-and-ceiling-lining-board-2-pack_p0497624)
cut into either crosswise 60 45x9x300 bits that can be chained together ($59/2/(2700/45)/0.3 = $1.64/m), or 6
45x9x2.7m strips ($59/2/6/2.7 = $1.82/m). Note these are hollow, hence chained bits would be like a
vented plastic batton.

[QuickBoard 300 x 9mm 2.7m Antique White PVC VJ-Crown
Reversible](https://www.bunnings.com.au/quickboard-300-x-9mm-2-7m-antique-white-pvc-vj-crown-reversible-2-pack_p0497612)
cut into 6 45x9x2.7m strips ($89/2/6/2.7 = $2.74/m).

[Brutus 6 x 38mm x 3m Building Moulding Cover
Trim](https://www.bunnings.com.au/brutus-6-x-38mm-x-3m-building-moulding-cover-trim_p1100628)
$10.92/3=$3.64/m

XPS foam! This is a DIY version of [Ametalin 2750x43x12mm ThermalBreak
strips](https://www.bunnings.com.au/ametalin-2750mm-x-43mm-x-12mm-thermalbreak-strips-r0-25-pack-of-50_p0401288)
which cost $458.07/(50x2.75) = $3.33/m. Compression strength is about 200kPa,
so a 70x50mm patch can take about 71kg or a 50mm strip can take more than 1000Kg/m.  Note foilboard compression
strength is about 70kPa so about 250kg/m on a 35mm wide joist. A 1200x600x50mm
sheet cut into 50 1200x50x9.5mm battens (table saw 2.5mm swarf) or 60
1200x50x10 battens (hotwire) ($29.8/(50x1.2) = $0.50/m).

https://www.bunnings.com.au/bastion-1200-x-600-x-50mm-xps-multi-use-foam-board_p0461084

Fluteboard! It looks very similar to vented cavity battens. Note it can also
be used as a cavity closer! The following cavity battens and all the related
products look like they have been made from laminated fluteboard;

https://www.ventsystems.com.au/products/vb20-wall-cavity-batten/
https://proctorgroup.com.au/construction-membranes/proctorpassive-drainage-batten-db-fr/

It's hard to get data on compression strength, but it looks like it will be
between 140kPa and 1.4MPa(???) Testing a 4x5cm piece of corflute it took about
30Kg before it collapsed. Thats 30*9.81/(0.05*0.04)=147150Pa=147kPa which
matches the 140kPa number above. A 70x50 patch can take only about 50Kg, or
for a 50mm strip about 713Kg/m. As per the cavity battens, it seems 4mm holes
are a sweet spot to prevent capilary action and block pests, so the
1200x900x5mm $14 tunnelcore is the thinest you'd want. There is also
2250x1220x8mm $35, which gives a bigger gap, but the holes a bigger and might
need a mesh. Note metal mesh with <2mm holes is a requirement for fire safety
to protect against embers, so maybe we need a mesh anyway.

You might want to stack 2x5mm for 10mm or 4x5mm for 20mm, if you do you could
"brick" the layers to get wider than 900mm lengths. Unfortunately
polypropyline is a bitch to glue;

https://forgeway.com/learning/blog/bonding-polypropylene-with-glue

There are special polypropyline glues but they are complicated and very
expensive. Corflute suggests hot glue or double sided tape. Other sites
suggest contact-adhesive. I've seen suggestions to use welding with a hot-air
gun, which would work well but might be very hard to do properly without
deforming everything. There is also triple-wall fluteboard available
(2200x1100x10mm $55.30, min purchase 5 for $276.49), but it's harder to find;

https://www.silverback.com.au/FLUTEB/Flute-Board-Gorilla-Sheets/pd.php?srsltid=AfmBOooX6iH3sJw21ZrMOS8uKxab1iDnLcwN4JPgcr-wDrPgkymtTRXr

Note that ultimately these will be mechanically fixed together with the
wall/roof mounting screws that go through to the frame/batton, so the strength
of the laminating bond probably doesn't matter much. Perhaps a light
heat-weld, contact adhesive, or double-sided-tape would be enough?

Testing with cheap double-sided tape, expensive double-sided tape, and cheap
contact adhesive, they all worked really well, way better than is required. I
suspect this is because the white tunnelcore is "corona treated" to make the
surface easier to print on.

Cutting a 1200x900x5mm sheet and laminating two layers can give 13 900x45x10mm
battens ($14/13/0.9 = $1.20/m), or can be "bricklayed" into longer battens.

2440x1220x5mm sheets can be bought on ebay, but only in packs of 10 for $340.

Using a single layer 2250x1220x8mm cut into 50 1220x45x8mm battons $35/50/1.22
= $0.57/m

This could also be done using [Sunlite 8 1200x610x8mm Clear Twinwall
Polycarbonate Sheet](https://www.bunnings.com.au/sunlite-8-1-2-x-0-61m-clear-twinwall-polycarbonate-sheet-1200mm_p1010852)
giving 25 0.61mx45x8mm battens ($29.76/25/0.61 = $1.95/m), or [Sunlite 10mm
Twinwall 1000x980x10mm Clear Polycarbonate Roofing $36.80
](https://www.bunnings.com.au/sunlite-10mm-twinwall-x-1-0m-clear-polycarbonate-roofing-1000mm_p1010830)
giving 21 0.91mx45x10mm battens ($36.80/21/0.91 = $1.93/m).

Finally, what about cutting strips of foilboard to use as a cavity batten?
cheap, and dispite the good enough compression strength, too easy to snap to
be worth even trying? The 10mm foilboard is a tiny bit cheaper than 8mm
tunnelcore per m^2.

#### Ventilation and Drainage

The http://ventsystems.com.au/ provides both an awesome set of ventilation
products, and a wealth of information on design and standards. Sadly their
products don't seem easy to get, and are probably really expensive. Their docs
pointed me at the existing standards, which are also freely available and very
good;

https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions

Standards say for a <10deg traditional mono-pitched roof requires 25000mm^2/m
at opposing ends of the roof. That's effectively a 25mm ventilation gap on the
entire length of the top and bottom sides of the roof.

For walls, NZ regs require cavity closers to have at least 1000mm^2/m at the
bottom. Top vents appear to be recommended but optional. I cannot find
Australian regs except related to fire protection which required metal mesh
with max 2mm openings to block embers from getting into the cavity. It seems
NZ regs are the leaders on wall cavity best practice.

The wall cavity gaps between foil/sarking is recommended to be 20mm, but with
profiled sheets the crests add their own 16mm cavity (avg 8mm gap). Also, the
20mm gap was largely to avoid "bulging of underlay" closing the gap, which
cannot happen with foilboard, and studies say a 10mm gap is probably
sufficient. Castelated cavity battens have 5mm deep gaps, and So I belive 9~10mm cavity battens would be sufficient for the
walls.

#### Tree holes

Holes for branches through treehouse walls, floors, and roofs need to be
somehow sealed against insects/rain/etc while still allowing the trees to grow
and move in the wind.

Holes at the floor level will have 40mm of clearance around the tree to allow
for alignment errors, tree growth, and movement.

Higher up in the tree branches are thinner and can move more, so we allow 50mm
of clearance.

Sealing the hole needs a flexible but robust seal against the tree to the roof
sheets, wall cladding, or floor. This needs to have a water-tight seal to the
external boards/sheets/cladding that will not interfere with the water flow.
It should also be robust enough to resist critters and have strong UV/weather
resistance.

Also, another layer of sealing should be done for the foilboard moisture
barrier, which should also be watertight. This should be protected by the
outer layers from critters/UV/weather, so it does not need to be as robust. It
needs to have a waterproof attachment to the foilboard.

The attachment to the tree needs to be waterproof without hurting the tree or
restricting growth and movement. This means it needs to have minimal (ideally
zero) holes/screws/etc into the tree, and be loose or stretchy enough to not
hurt tree growth and cause tree girdling injurys.

These suggest a flexible rubber membrane attached to the tree and treehouse
with butyle tape. To go around the tree it needs to be initially wrapped and
then joined to itself with a waterproof seam. Joins and seams can be
reenforced with pop-rivets through punched holes and small washers, and sealed
with butyle tape.

The butyle tape needs to be stretchy, without any fiber/fabric/aluminium
re-enforcement that limits the stretch. double-sided pure butyle looks to be
the best option.

For the outside, rubber tubes seem best. These are a UV and weather resistent
butyle rubber (I think) that is about 2mm thick. It should stick well with
butyle to both the tree and treehouse. The hard part is finding tubes big
enough? bunnings has wheelbarrow tubes up to 390mm outside, 200mm inside
diameter. Larger tubes seem hard to find.

Attaching the tubes to the roof/wall sheets can be done with rivets, but care
must be taken when riveting polycarbonate. The polycarbonate hole needs to be
1.5x the rivet diameter to avoid radial stresses and for thermal expansion,
and a backup washer with laminated rubber is recommended;

https://www.theplasticshop.co.uk/plastic_technical_data_sheets/lexan_polycarbonate_sheet_processing_guide.pdf

Another possiblity is plastic rivets. It might even be possible to 3D print my
own rivets, but [weather resistant
filaments](https://www.matterhackers.com/articles/the-best-3d-printing-filament-for-outdoor-use)
like
[ASA](https://www.inkstation.com.au/2102/asa-3d-filament-175mm-black-1kg-roll-p-24990.html#25329)
can be hard to work with. Would need a [high-temp
nozzle](https://www.ebay.com.au/itm/315402989256?itmmeta=01J45YHBKZ0SAY63BKA5N2J38T&hash=item496f7baec8:g:EBYAAOSwpXVmWDtJ&itmprp=enc%3AAQAJAAAAwDxHvR10Ss%2BxLtCmAw4vsBIM3ArTLn%2BCWKrAVQCjIUKp8KLDD41uV3v4X7OwedIIL7VO01823TXLC0wtrgdFgCNJqGP3tZtTF4Gzxi8U%2FHqiz%2FVLkJNHjSPPcV1JIsbXq5kfa27N%2BG9hDoE19VufBjNasQQ3OdeT73nL%2FGp1Xh%2BN5zzEaqiq3e10MS4qneL1f1cboaw9wYDYnwDap7QAGFnFDfmR75GnvxFZMqgDcyS4hM00ZexLdsnzJYd3s1IEXw%3D%3D%7Ctkp%3ABk9SR5K6xb6hZA).
I have now bought some ASA and a nozzle so I can print any required outdoor
parts.

For the inner seal, I was thinking silicone would be best; it's very weather
resistant and robust. However, it's hard to find in sheets thin enough, and
bonding to it is really really hard. I've tested butyle against my silicone
work mat and it really doesn't stick. Making it stick to itself and seal after
going around the tree will be really hard. I did find special primers that can
be used with super-glue for making silicone rubber stick, but it's literally
hundreds of dollars for a tiny bottle. Other types of rubber sheet are even
harder to find.

The ideal thickness/stretchyness is physio resistance bands. The come in a
variety of color-coded thicknesses 15cm wide rolls and are pretty cheap. They
are latex rubber, which doesn't have a good reputation against weather, but
being the under-layer moisture-barrier, maybe that doesn't matter. And
boy-oh-boy, does butyle stick to them! The rubber will literally rip before
coming free. rivet re-enforcemnts will not be required.

The tree hole sizes are (clockwise from trunk near origin) circumfrance is as
measured;

Note circ-i is tree circumfrance and circ-o is hole plus 30mm overlap outside
circumfrance.

hole   tree    gap Dmm  D"    circ-i  circ-o tubes
Floor1 360x340 40  ~340 13.4"   1030  1470   12"  1.5x
Floor2 240x230 40  ~240  9.4"    750  1190    8"  1x
Floor3 380x300 40  ~340 13.4"   1030  1470   12"  1.5x

WallR  247x166 50  ~210  8.3"    650  1150    8"  1x (half)
WallF  630x290 50  ~460 18.1"   1440  1940   16"  2x
			       	              
Roof2  295x208 50  ~240  9.4"    750  1250    8" 1x
Roof3a 275x225 50  ~250  9.8"    790  1290    8" 1x 
Roof3b 250x143 50  ~210  8.3"    650  1150    8" 1x
Roof4  280x280 50  ~280 11.0"    880  1380   10" 1x (half)

10 required, 2 per tube, = 5 tubes of bunnings Move It 650 x 8 $12.95 requred.
Alternatively, it might be good to get one big 16" for the wallF hole.

The inner diameter of these is 20cm (63cm circumfrance) and outer is about
38cm (120cm circumfrance) but can stretch the inner to 28cm (90cm
circumfrance), with a strip width of 13.2cm giving you two per tube. Note
inner+width!=outer diameter, because it's conical when flat.

kmart bike tubes are cheaper $6 each and in sizes 40/50/66/70/74 cm inside
diameter, but are only about 3cm wide? The $10 66x4.8cm one is a tiny bit
wider, but not enough. Even motorbike tubes are not wide enough. Unfortunately
car tubes seem to be hard to find (there are some on ebay) and more expensive.

The total (inner) circumfrence length is 8.1m, and the outer length (not
including attachment border) is 10.7m. Adding attachment border is about
13~14m So we need about 15m of 15cm wide latex strip, and about 6 bunnings
tubes.

#### Windows

Docs online have lots of different recommendations.

Lots of docs say it's important to have sloped sills AND backdams. Some say
sloped sills OR backdams. Some say to use manufactured kit or sheet metal sill
pan flashing. Others say to use wall wrap and self adhesive membrane or tape
flashing over the rough opening.

The rough opening can be sloped using either a sloped sill-wedge on top of the
rough opening sill plate, sloping the sill plate by cutting an angle on the
cripple stud ends, or ripping an angle to the top of the sill plate. A backdam
can be added with strip of wood or self-adhesive gasket.

The sill-wedge slope should be at least 1:15 (3.8deg) with 5deg (7:80 or
~1:11) being commonly used. The recommended minimum slope for drainage of
window sills is 1/4 (14deg or roughly 15deg), but also 1/8 (7deg) is common.

Older designs have a full windowsill on top of the sill plate with a 1/4 slope
(14deg) and drip-cut on the bottom. But this doesn't seem to work well with
modern aluminium windows. These are typically used when building the window
in-place and the sill forms the bottom of the window frame, but I've seen some
wooden units with bottoms sloped to sit on a sloped sill (or sloped sill
plate?).

Most window installation docs just have a flat rough opening with flashing, no
slope or backdam. Most standard windows have a flat base, so installing them
in a sloped opening requires sloped packing shims. Note that shims are not
supposed to go the full width of the sill-plate, and the gap between shims and
the sill-plate and reveals is important for drainage;

https://www.appliedbuildingtech.com/system/files/nrc-irc_window_sill_details_for_effective_drainage_of_water.pdf

https://cdnassets.hw.net/dd/3c/e598bb1e45c9af6481862c7a85ed/2010-04-bateman.pdf

https://www.marvin.com/blog/10-most-common-window-installation-mistakes

Aluminium windows often have a narrow frame with nailing fins to mount them
from outside flush against the wrapped rough openening which can then be
sealed against the wall membrane with flashing tape. Or sometimes the fins are
attached to the reveals which are then screwed to the rough opening, with
flashing and/or flashing tape used to seal the gap between the fins and the
outside edge of the rough opening, similar to how prefabricated timber framed
windows are installed. This doesn't work well with a full sill in place, and
the windows have their own integrated minimalistic sill and window trim
designed to sit over the cladding. Sometimes a false sill is installed under
the window for the look and/or to drain the water away from the cladding.
Reveals are used to line and seal the inside of the window cavity against the
aluminium frame, with different reveal widths for different wall thicknesses.

Wooden window units tend to have the internal reveal integrated and no
mounting fins. Instead they are inserted from the inside and screwed to the
rough opening sides through the integrated reveals with them flush to the
inside wall lining. The integrated reveal+frame should be wide enough so the
outside edge of the frame aligns or slightly protudes past the external
cladding.

https://www.bunnings.com.au/diy-advice/home-improvement/doors-windows/how-to-install-a-timber-awning-window
https://www.stockwindows.com.au/product/timber-awning-window-600h-x-1210w-2/

Undersides of sills, sashes, and heads should have drip groves cut, about 2~3mm
wide, 2~4mm deep, and about 7mm back from the edge.

##### Double glazing

Glass can be 4mm to 10mm thick, with higher thicknesses helping insulation of
both heat and sound. There are also special insulating/tinted/etc glasses.

Gaps can be filled with (in increasing cost/quality) air, argon, krypton or
vacuum. Gaps can be 6 to 20mm, with the ideal gap depending on the gas and
heat vs sound insulation objectives. Bigger gaps insulate sound better, but
there is an ideal gap per gas for insulation (to small gives conduction, too
big gives convection). It seems 12mm is the sweet spot for air/argon, but many
argue 14mm or 16mm is better.

4mm glass/10mm gap/4mm glass seems common.

Aim for 12mm gap.

Also need desicant to absorb moisture. 


### Braiding

I used braided macrame cord to make straps to wrap around the trees above
their entry into the treehouse as "chain drains" to divert water running down
the trunks away before it gets to the entry hole.

It's useful to know how much longer the cord needs to be. A 4-strand flat
braid uses 1.5x, a 4-strand circular braidabout 1.3x the cord length. Macrame
with 4 strands uses 4x the length for the outer strands, so by switching the
inner and outer strands periodically it averages 2.5x the chord length. Using
a mixture of braiding and macrame it's possible to create varying densities.

## Indexes

### Definitions

TLA

:   Three letter acronyms.

aterm

:   a definition of the term.

### References

-   <http://related.com/url>

------------------------------------------------------------------------

<http://project/url/DESIGN> \$Id: DESIGN,v 221032f84299 2021/03/12
00:34:53 abo \$
