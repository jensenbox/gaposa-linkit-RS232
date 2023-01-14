import serial

BANK_A = 0x00
BANK_B = 0x01
BANK_C = 0x02

CHANNEL_1 = 0x01
CHANNEL_2 = 0x02
CHANNEL_3 = 0x03
CHANNEL_4 = 0x04
CHANNEL_5 = 0x05
CHANNEL_6 = 0x06
CHANNEL_7 = 0x07
CHANNEL_8 = 0x08

COMMAND_ADD_MOTOR = 0xAA
COMMAND_DELETE_MOTOR = 0xAB
COMMAND_PRESET = 0xAD
COMMAND_TILT_UP = 0xBA
COMMAND_TILT_DOWN = 0xBB
COMMAND_STOP = 0xCC
COMMAND_UP = 0xDD
COMMAND_DOWN = 0xEE


def send_instruction(bank, channel, command):
    instructions = [0x67, bank, channel, command]

    checksum = 0x00
    for instruction in instructions:
        checksum ^= instruction

    instructions.append(checksum)

    binary_date = bytes(instructions)

    print("Instructions: %s" % instructions)
    print("Checksum: %s" % checksum)
    print("Binary Data: %s" % binary_date)

    with serial.Serial(
            port='/dev/ttyS0',
            baudrate=9600,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=5
    ) as serial_port:
        serial_port.write(binary_date)
        response = serial_port.read(3)

    print("Response: %s" % response)


if __name__ == '__main__':
    send_instruction(BANK_A, CHANNEL_1, COMMAND_DOWN)
