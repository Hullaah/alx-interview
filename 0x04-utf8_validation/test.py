validUTF8 = __import__('0-validate_utf8').validUTF8

# Test Case 1: Valid 1-byte UTF-8 character (ASCII)
assert validUTF8([0b01111111]) == True  # 1-byte, valid ASCII character (127)

# Test Case 2: Valid 2-byte UTF-8 character
assert validUTF8([0b11000010, 0b10100010]) == True  # '¢' (U+00A2)

# Test Case 3: Valid 3-byte UTF-8 character
assert validUTF8([0b11100010, 0b10000010, 0b10101100]) == True  # '€' (U+20AC)

# Test Case 4: Valid 4-byte UTF-8 character
assert validUTF8([0b11110000, 0b10010000, 0b10001100, 0b10011111]) == True  # '𐍟' (U+1039F)

# Test Case 5: Invalid UTF-8 (invalid continuation byte in a 2-byte sequence)
assert validUTF8([0b11000010, 0b11000010]) == False  # Continuation byte should start with `10`

# Test Case 6: Invalid UTF-8 (overlong encoding)
assert validUTF8([0b11000000, 0b10000000]) == False  # Overlong encoding for ASCII character 0

# Test Case 7: Invalid UTF-8 (missing continuation byte)
assert validUTF8([0b11100010, 0b10000010]) == False  # Missing last byte for 3-byte character

# Test Case 8: Valid mix of 1-byte, 2-byte, and 3-byte characters
assert validUTF8([0b01111111, 0b11000010, 0b10100010, 0b11100010, 0b10000010, 0b10101100]) == True

# Test Case 9: Invalid 4-byte character (out of bounds for UTF-8 range)
assert validUTF8([0b11110101, 0b10101111, 0b10111111, 0b10111111]) == False  # Code point U+15FFFF, out of UTF-8 range

# Test Case 10: Surrogate code points (should be invalid in UTF-8)
assert validUTF8([0b11101101, 0b10100000, 0b10000000]) == False  # Surrogate range U+D800

# Test Case 11: Empty input (edge case)
assert validUTF8([]) == True  # No data, considered valid

# Test Case 12: Random invalid bytes (not starting with valid leading bits)
assert validUTF8([0b10000000, 0b11000000]) == False  # Invalid start for UTF-8 sequence
