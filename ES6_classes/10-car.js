export default class Car {
  constructor(brand, motor, color) {
    /* eslint-disable */
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    /* eslint-enable */
  }

  cloneCar() {
    /* check for Symbol.species if not found it return normal constructor */
    const Constructor = this.constructor[Symbol.species] || this.constructor;
    return new Constructor();
  }
}
