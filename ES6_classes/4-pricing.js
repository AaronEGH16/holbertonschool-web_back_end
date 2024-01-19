import Currency from './3-currency';

export default class Pricing {
  constructor(amount = 0, currency = Currency) {
    this.amount = amount;
    this.currency = currency;
  }

  displayFullPrice() {
    return `${this.amount} ${(this.currency).name} (${(this.currency).code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number') {
      throw TypeError('Amount must by a number');
    }
    if (typeof conversionRate !== 'number') {
      throw TypeError('Conversion Rate must by a number');
    }
    return amount * conversionRate;
  }

  get amount() {
    /* eslint-disable */
    return this._amount;
    /* eslint-enable */
  }

  get currency() {
    /* eslint-disable */
    return this._currency;
    /* eslint-enable */
  }

  set amount(val) {
    if (typeof val !== 'number') {
      throw TypeError('Amount must by a number');
    }
    /* eslint-disable */
    this._amount = val;
    /* eslint-enable */
  }

  set currency(val) {
    /* eslint-disable */
    this._currency = val;
    /* eslint-enable */
  }
}
