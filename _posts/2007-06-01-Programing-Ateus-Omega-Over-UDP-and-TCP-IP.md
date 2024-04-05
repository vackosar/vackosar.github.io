---
layout: post
title: Programing Ateus Omega Over UDP and TCP/IP
date: 2007-06-01
image: /images/Ateus-Omega-UART-dsPIC-SPI-ENC28J60-UDP-TCP-IP-Programing.png
categories: electronics
description: Replacing Xapi server program, designed for remote programming of the Ateus Omega control panel via the Internet, with a module directly built into the control panel, thus eliminating the problem of dependence on a switched-on computer
permalink: /:categories/:title
---


![Ateus Omega via UART to dsPIC via SPI to ENC28J60 via IP](/images/Ateus-Omega-UART-dsPIC-SPI-ENC28J60-UDP-TCP-IP-Programing.png)

### Authors
Vaclav Kosar, Jan Kapic


### Abstract
The aim of our work was to replace the Xapi server program, designed for remote
programming of the Ateus Omega control panel via the Internet, with a module that will be
built directly into the control panel, thus eliminating the problem of dependence on a
switched-on computer. Basically, it is a simple passive network card, which also
communicates with the control panel (Serial port).

### Introduction
The goal of our long-term graduation thesis was to design and build a "hardware
Xapi server". The Xapi server is a software utility that allows the control panel to
communicate
with other computers on the Internet. The disadvantage of this method lies in the nature of
the whole solution to the problem - the Xapi server is a program and therefore depends on
the running computer. We have tried to eliminate this disadvantage by replacing the Xapi
server with our module, which will be built directly into the control panel. The basic
questions of the whole work were:

1. How to connect DsPIC with Ethernet and how to work with its protocols?
2. How to connect the DsPIC to the control panel via serial port (connector wiring,
voltage levels) ?
3. What changes in data occur during the Ethernet to Serial port transition?


The first question was solved by using the ENC28J60 integrated circuit, which
works as an Ethernet controller operating on layers 1 and 2 of the OSI model, studying the
relevant issues and building a package of programs for DsPIC capable of processing data
of higher protocols. Which was programmatically and time-consuming, but possible with
complete documentation for the future.


The second question was solved by measuring the control panel connector for
communication modules and redrawing the wiring of the existing module for RS232
communication.

The third problem was significantly more complicated than the others. We
attempted to eavesdrop on the Xapi server's communication with both interfaces, but we
were unable to detect any major continuities in the output data. It was only by comparing
the data in the TCP packets when programming with the Xapi server and the data sent by
the computer when "normally" programming the control panel directly using the Omega
program that we began to discover connections. Unfortunately this was not enough, so we
were forced to ask for the original documentation for the serial communication of the
control panel from the manufacturer - 2N. With the catalogue sheets we received, we
could finally work out the first ideas of the whole solution. However, the CRC32 counting
was still an issue.

This was followed by a progression in hardware and software design. Thanks to the
training board we made the first DsPIC - ENC connection. The first programs for serial
5-communication were created. The problem with CRC32 was solved just before the creation
of the final PCB (MEDEA MODULE) thanks to the great commitment of Professor
Kubalik (more about CRC32 in the relevant chapter). Unfortunately, although the program
for communication via TCP/IP was almost complete, we were forced to choose a simpler variant due to time constraints, and
therefore the control panel is programmable only via UDP.

Nevertheless, the Médea module fulfils its function - our work was therefore successful,
and in the full version of the assignment.

### Conclusion
The result of our long-term graduation work is a fully functional hardware module
for the Ateus Omega control panel. By constructing this product, we have honed a number
of skills including: programming in Assembler, circuit board fabrication, monitoring and
applying packet communication protocols in practice, and teamwork. We learned how to
solve problems related to product implementation. A possible future improvement could be
to reduce the power dissipation of the voltage regulator. Finally, we would like to thank
Professor Ing. T. Kubalík for his support and help
at a time when the situation seemed unsolvable.


[Full MATRICULATION EXAM Thesis](/docs/mat_prace_MEDEA_MODUL_en.pdf)
