export default class Airport {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  set name(val) {
    if (typeof val !== 'string') throw TypeError('Name must by a string');
    /* eslint-disable */
    this._name = val;
    /* eslint-enable */
  }

  set code(val) {
    if (typeof val !== 'string') throw TypeError('Code must by a string');
    /* eslint-disable */
    this._code = val;
    /* eslint-enable */
  }

  get name() {
    /* eslint-disable */
    return this._name;
    /* eslint-enable */
  }

  get code() {
    /* eslint-disable */
    return this._code;
    /* eslint-enable */
  }

  toString() {
    return `[object ${this.code}]`;
  }
}
