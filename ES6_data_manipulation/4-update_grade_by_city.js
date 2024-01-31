const updateStudentGradeByCity = (students, city, newGrades) => students
  .filter((student) => student.location === city)
  .map((student) => {
    const newGrade = newGrades.find(
      (grade) => grade.studentId === student.id,
    );
    return {
      ...student,
      grade: newGrade ? newGrade.grade : 'N/A',
    };
  });

export default updateStudentGradeByCity;
