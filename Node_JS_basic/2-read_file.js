const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const headers = lines[0].split(',');
    const studentsByField = {};

    for (let i = 1; i < lines.length; i += 1) {
      const fields = lines[i].split(',');
      const field = fields[headers.indexOf('field')];
      const firstName = fields[headers.indexOf('firstname')];

      if (field && firstName) {
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
      }
    }

    console.log(`Number of students: ${lines.length - 1}`);

    for (const [field, names] of Object.entries(studentsByField)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
