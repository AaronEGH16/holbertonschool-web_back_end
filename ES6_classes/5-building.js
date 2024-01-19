export default class Building {
  constructor(sqft) {
    /* eslint-disable */
    this._sqft = sqft;
    /* eslint-enable */
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    /* eslint-disable */
    return this._sqft;
    /* eslint-enable */
  }

  set sqft(Sqft) {
    if (typeof Sqft === 'number') {
      /* eslint-disable */
      this._sqft = Sqft;
      /* eslint-enable */
    } else {
      throw TypeError('Sqft must by a number');
    }
  }
}
