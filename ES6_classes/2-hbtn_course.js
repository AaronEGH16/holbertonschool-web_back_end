export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  set name(Name) {
    if (typeof Name !== 'string') {
      throw TypeError('Name must be a string');
    }
    /* eslint-disable */
    this._name = Name;
    /* eslint-enable */
  }

  set length(Length) {
    if (typeof Length !== 'number') {
      throw TypeError('Length must be a number');
    }
    /* eslint-disable */
    this._length = Length;
    /* eslint-enable */
  }

  set students(Students) {
    if (Array.isArray(Students)
          && Students.every((student) => (typeof student === 'string') === true)) {
      /* eslint-disable */
      this._students = Students;
      /* eslint-enable */
    } else {
      throw TypeError('Students must be an array of strings');
    }
  }

  get name() {
    /* eslint-disable */
    return this._name;
    /* eslint-enable */
  }

  get length() {
    /* eslint-disable */
    return this._length;
    /* eslint-enable */
  }

  get students() {
    /* eslint-disable */
    return this._students;
    /* eslint-enable */
  }
}
