const createInt8TypedArray = (length, position, value) => {
  const buffer = new ArrayBuffer(length);
  const arrayView = new Int8Array(buffer);
  try {
    arrayView[position] = value;
  } catch (error) {
    throw new Error('Position outside range');
  }
  return new DataView(buffer);
};

export default createInt8TypedArray;
