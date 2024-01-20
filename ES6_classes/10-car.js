export default class Car {
  constructor(brand, motor, color) {
    /* eslint-disable */
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    /* eslint-enable */
  }

  cloneCar() {
    return new this.constructor();
  }
}
