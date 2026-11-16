import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const input = await FileBlob.load("../../CRM/DS CHỨC NĂNG CRM.xlsx");
const workbook = await SpreadsheetFile.importXlsx(input);
const sheet = workbook.worksheets.getItem("DS CHỨC NĂNG CRM");
const rows = sheet.getRange("A1:K422").values;

const featureRows = rows.slice(2).map((row, index) => ({
  row: index + 3,
  tt: row[0],
  code: row[1],
  module: row[2],
  name: row[3],
  description: row[4],
  status: row[5],
  result: row[8],
  note: row[9],
}));

const moduleCounts = {};
for (const row of featureRows) {
  const key = row.module || "(blank)";
  moduleCounts[key] = (moduleCounts[key] || 0) + 1;
}

const headings = featureRows.filter(row => row.name != null && String(row.name).trim() !== "");
console.log(JSON.stringify({ moduleCounts, headings }, null, 2));
