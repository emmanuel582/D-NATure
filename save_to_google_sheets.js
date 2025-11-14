// Google Sheets API integration for saving user registration data
// 1. This script will use Google Apps Script as a web endpoint
// 2. The endpoint will receive a POST request from the site and save the data to a Google Sheet

function doPost(e) {
  var sheet = SpreadsheetApp.openById('YOUR_SHEET_ID').getSheetByName('Sheet1');
  var data = JSON.parse(e.postData.contents);
  sheet.appendRow([
    new Date(),
    data.firstName,
    data.otherNames,
    data.email,
    data.primaryPhone,
    data.whatsappNumber,
    data.address,
    data.occupation,
    data.otherOccupation,
    data.dob,
    data.age,
    data.gender
  ]);
  return ContentService.createTextOutput('Success').setMimeType(ContentService.MimeType.TEXT);
}
