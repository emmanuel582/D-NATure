// Google Sheets API integration for saving user registration data
// 1. This script will use Google Apps Script as a web endpoint
// 2. The endpoint will receive a POST request from the site and save the data to a Google Sheet

function doPost(e) {
  var sheet = SpreadsheetApp.openById('YOUR_SHEET_ID').getSheetByName('Sheet1');
  var data = JSON.parse(e.postData.contents);
  sheet.appendRow([
    data.DATE,
    data.FirstName,
    data.LastName,
    data.Gmail,
    data.PhoneNumber,
    data.WhatsappNumber,
    data.Address,
    data.Occupation,
    data.Gender,
    data.DateOfBirth,
    data.AGE,
    data.Gender,
    data.SelectedPack,
    data.TotalAmount,
    data.SubscriptionDuration,
    data.PayoutDuration
  ]);
  return ContentService.createTextOutput('Success').setMimeType(ContentService.MimeType.TEXT);
}
