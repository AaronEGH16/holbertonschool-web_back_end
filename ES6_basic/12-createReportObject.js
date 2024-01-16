export default function createReportObject(employeesList) {
  const allEmployees = {};

  // Loop through the properties of the employeesList object
  for (const department in employeesList) {
    // Verify that it belongs to the object's properties and not its prototype
    if (Object.prototype.hasOwnProperty.call(employeesList, department)) {
      // Fill the allEmployees object with the obtained properties
      allEmployees[department] = [...employeesList[department]];
    }
  }

  return {
    allEmployees,
    // Get the number of keys inside the allEmployees object to return it
    getNumberOfDepartments() {
      return Object.keys(allEmployees).length;
    },
  };
}
