#include "encrypt.h"
#include <random>

using namespace gamit;

byte_t CEncrypto::_mask = 108;

void CEncrypto::simpleEncrypt(std::string & src)
{
	__mask(src);
	__encrypt(src);
}

void CEncrypto::simpleDecrypt(std::string & src)
{
	__decrypt(src);
	__mask(src);
}

void CEncrypto::__mask(std::string & src)
{
	if (src.empty())
	{
		return;
	}

	unsigned maxIdx = src.size() - 1;

	for (unsigned i = 0; i <= maxIdx; i += 2)
	{
		if (i == maxIdx)
		{
			src[i] ^= _mask;
			return;
		}

		byte_t bi = src[i];
		byte_t bj = src[i + 1];

		bi ^= _mask;
		bj ^= _mask;

		src[i] = bj;
		src[i + 1] = bi;
	}
}

void CEncrypto::__encrypt(std::string & src)
{
	if (src.empty())
	{
		return;
	}

	byte_t pivot = byte_t(std::rand() % 127 + 1);
	src.push_back(pivot);

	for (int i = int(src.size() - 2); i >= 0; i--)
	{
		src[i] ^= pivot;
		pivot = src[i];
	}
}

void CEncrypto::__decrypt(std::string & src)
{
	if (src.empty())
	{
		return;
	}

	for (byte_t i = 0; i < src.size() - 1; i++)
	{
		src[i] ^= src[i + 1];
	}

	src.pop_back();
}
