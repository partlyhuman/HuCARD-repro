# TL866 II adapter

This is an adapter for the popular [TL866 II](http://www.xgecu.com/EN/TL866_main.html) programmer, and likely works with the others in this line as well.

Ichigo created a programming adapter along with this HuCard repro, but it was for Willem and GQ4x programmers, necessitating this new adapter.

Thankfully, there is now a commercially available (and reasonably priced!) HuCard cartridge slot from JT Studios. This programmer is developed around it.

### BOM

* 1x PCB, [gerber files](production/) available here
* 2x row 2.54mm pitch header pins, 16 pins or cut down to 16 pins
* 1x [JT Studios PC Engine cartridge slot](https://jt-studios.com/product/38pin-pc-engine-connector/)

Tested with SST39SF040 flash, simply program as if you're directly programming the chip. Ichigo's HuConv program may be used, but I haven't really encountered a .PCE file in the wild that needed any processing.