import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }

  set floors(val) {
    if (typeof val !== 'number') {
      throw TypeError('floors must by a number');
    }
    /* eslint-disable */
    this._floors = val;
    /* eslint-enable */
  }

  get floors() {
    /* eslint-disable */
    return this._floors;
    /* eslint-enable */
  }
}
