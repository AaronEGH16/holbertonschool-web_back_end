const createInt8TypedArray = (length, position, value) => {
  if (position < 0 || position > length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const arrayView = new Int8Array(buffer);

  arrayView[position] = value;

  return new DataView(buffer);
};

export default createInt8TypedArray;
