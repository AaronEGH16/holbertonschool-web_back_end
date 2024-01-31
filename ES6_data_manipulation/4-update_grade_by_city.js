const updateStudentGradeByCity = (students, city, newGrades) =>
  students
    .filter((student) => student.location === city)
    .map((student) => {
      const newGrade = newGrades.find(
        (grade) => grade.studentId === student.id
      );
      student.grade = newGrade ? newGrade.grade : "N/A";
      return student;
    });

export default updateStudentGradeByCity;
