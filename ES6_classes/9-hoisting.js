export class HolbertonClass {
  constructor(year, location) {
    /* eslint-disable */
    this._year = year;
    this._location = location;
    /* eslint-enable */
  }

  get year() {
    /* eslint-disable */
    return this._year;
    /* eslint-enable */
  }

  get location() {
    /* eslint-disable */
    return this._location;
    /* eslint-enable */
  }
}

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    /* eslint-disable */
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
    /* eslint-enable */
  }

  get fullName() {
    /* eslint-disable */
    return `${this._firstName} ${this._lastName}`;
    /* eslint-enable */
  }

  get holbertonClass() {
    return this.holbertonClass;
  }

  get fullStudentDescription() {
    /* eslint-disable */
    return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
    /* eslint-enable */
  }
}

const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');

const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
const student2 = new StudentHolberton('John', 'Doe', class2020);
const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
const student4 = new StudentHolberton('Donald', 'Bush', class2019);
const student5 = new StudentHolberton('Jason', 'Sandler', class2019);

const listOfStudents = [
  student1,
  student2,
  student3,
  student4,
  student5,
];

export default listOfStudents;
