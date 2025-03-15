const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');  
    const lines = data.split('\n').filter(line => line.trim() !== '');

    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    const fields = lines[0].split(',');
    const f_counts = {};

    fields.forEach(field => {
      f_counts[field] = [];
    });

    for (let i = 1; i < lines.length; i++) {
      const student = lines[i].split(',');

      if (student.length !== fields.length) continue;

      student.forEach((value, index) => {
        const field = fields[index];
        if (value.trim()) {
          f_counts[field].push(value.trim());
        }
      });
    }

    const total = Object.values(f_counts).reduce((acc, students) => acc + students.length, 0);
    console.log(`Number of students: ${total}`);

    fields.forEach(field => {
      const students_f = f_counts[field];
      console.log(`Number of students in ${field}: ${students_f.length}. List: ${students_f.join(', ')}`);
    });

  } catch (err) {
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
