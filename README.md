# gaposa-linkit-RS232
A simple script communicate with the Gaposa LinkIt RS-232 

The documentation for the unit can be found as links from https://www.gaposa.it/eng/linkit/

Example output:

    Instructions: [103, 0, 1, 238, 136]
    Checksum: 136
    Binary Data: b'g\x00\x01\xee\x88'
    Response: b''

To help with the debugging, set up a virtual port:

    socat -x -v /dev/ttyS0,rawer,b9600,crnl PTY,link=/tmp/ttyV1,rawer,crnl

Socat output will look like:

    < 2023/01/13 22:42:55.539238  length=5 from=0 to=4
     67 00 01 ee 88                                   g....
    --
    < 2023/01/13 22:44:09.596044  length=5 from=5 to=9
     67 00 01 aa cc                                   g....
    --
