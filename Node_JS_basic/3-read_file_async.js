const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        // Diviser le contenu en lignes et filtrer les lignes vides
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        // Vérifier s'il y a des données (au moins l'en-tête)
        if (lines.length <= 1) {
          console.log('Number of students: 0');
          resolve();
          return;
        }

        // Retirer l'en-tête (première ligne)
        const students = lines.slice(1);

        // Compter le nombre total d'étudiants
        console.log(`Number of students: ${students.length}`);

        // Organiser les étudiants par domaine
        const fields = {};

        students.forEach((line) => {
          const [firstname, , , field] = line.split(',');

          // Vérifier que la ligne contient toutes les données nécessaires
          if (firstname && field) {
            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(firstname);
          }
        });

        // Afficher le nombre d'étudiants par domaine avec la liste des prénoms
        Object.keys(fields).forEach((field) => {
          const studentList = fields[field];
          console.log(
            `Number of students in ${field}: ${
              studentList.length
            }. List: ${studentList.join(', ')}`,
          );
        });

        resolve();
      } catch (parseError) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
