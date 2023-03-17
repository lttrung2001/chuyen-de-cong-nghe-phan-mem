# Thành viên:
# 1. Lê Thành Trung - N19DCCN214
# 2. Đinh Trường Sơn - N19DCCN159
# 3. Trần Quang Ngọc Huỳnh - N19DCCN075
def vb_encode_number(number):
	bytes = []
	while True:
		bytes.insert(0, number % 128)
		if number < 128:
			break
		number //= 128
	bytes[len(bytes) - 1] += 128
	return bytes


def vb_encode(numbers):
	byte_stream = []
	for number in numbers:
		bytes = vb_encode_number(number)
		byte_stream.extend(bytes)
	return byte_stream


def vb_decode(byte_stream):
	numbers = []
	n = 0
	for i in range(len(byte_stream)):
		if byte_stream[i] < 128:
			n = 128 * n + byte_stream[i]
		else:
			n = 128 * n + (byte_stream[i] - 128)
			numbers.append(n)
			n = 0
	return numbers


if __name__ == '__main__':
	number = 12834
	arr_input = [int(x) for x in str(number)]
	encoded = vb_encode(arr_input)
	decoded = vb_decode(encoded)
	arr_output = [str(x) for x in decoded]

	print(f'{encoded=} {decoded=}')
	print(int(''.join(arr_output)))
