export default class Currency {
  constructor(code = '', name = '') {
    this.code = code;
    this.name = name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }

  set code(Code) {
    if (typeof Code !== 'string') {
      throw TypeError('Code must by a String');
    }
    /* eslint-disable */
    this._code = Code;
    /* eslint-enable */
  }

  set name(Name) {
    if (typeof Name !== 'string') {
      throw TypeError('Name must by a String');
    }
    /* eslint-disable */
    this._name = Name;
    /* eslint-enable */
  }

  get code() {
    /* eslint-disable */
    return this._code;
    /* eslint-enable */
  }

  get name() {
    /* eslint-disable */
    return this._name;
    /* eslint-enable */
  }
}
