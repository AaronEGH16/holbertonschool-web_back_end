export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  set size(val) {
    if (typeof val !== 'number') throw TypeError('size must by a number');
    /* eslint-disable */
    this._size = val;
    /* eslint-enable */
  }

  set location(val) {
    if (typeof val !== 'string') throw TypeError('location must by a string');
    /* eslint-disable */
    this._location = val;
    /* eslint-enable */
  }

  get size() {
    /* eslint-disable */
    return this._size;
    /* eslint-enable */
  }

  get location() {
    /* eslint-disable */
    return this._location;
    /* eslint-enable */
  }

  valueOf() {
    return this.size;
  }

  toString() {
    return this.location;
  }
}
