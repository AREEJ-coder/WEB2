// ============================Credit Card Mask=======================
function maskify(cc) {
  const visibleLength = Math.max(0, cc.length - 4);
  const maskedPart = "#".repeat(visibleLength);
  const lastFourDigits = cc.slice(-4);

  return maskedPart + lastFourDigits;
}
// ===============================Remove First and Last Character======

function removeChar(str) {
  return str.slice(1, -1);
}
// =======================DNA to RNA Conversion================
function DNAtoRNA(dna) {
  // create a function which returns an RNA sequence from the given DNA sequence
  let rna = "";
  for (let i = 0; i < dna.length; i++) {
    if (dna[i] === "T") {
      rna += "U";
    } else {
      rna += dna[i];
    }
  }
  return rna;
}
// ===================Jenny's secret message======================

function greet(name) {
  if (name === "Johnny") return "Hello, my love!";

  return "Hello, " + name + "!";
}
// ===============If you can't sleep, just count sheep!!==============
var countSheep = function (num) {
  let result = "";
  for (let i = 1; i <= num; i++) {
    result += `${i} sheep...`;
  }
  return result;
};
