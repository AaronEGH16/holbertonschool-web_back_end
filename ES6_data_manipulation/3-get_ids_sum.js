const getStudentIdsSum = (students) => students.reduce((res, student) => res + student.id, 0);

export default getStudentIdsSum;
