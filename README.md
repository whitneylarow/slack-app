# Slack Application

This is the repo for a Heroku web application that fetches and display source code from any web page. The app displays a summary of source code through a list of HTML tags and the count of these tags. Clicking on tags highlights their instances in the source code.

For more specifications, see Slack's [Application Engineer Coding Exercise](https://slack-files.com/T024BE7LD-F0BPHNBAR-67ccd61806).

Implementation nuances:
1. Tags included in the count:
    * Beginning tags
    * Tags within comments
2. Tags excluded in the count:
    * Tags beginning with `!`, `?`, or other non-word characters (e.g. `<!DOCTYPE html>` and `<?proc ... >`)
    * Tags within `<script>` tags (these would presumably be JavaScript, not HTML)
3. Only beginning tags are highlighted
4. Highlighting doesn't ignore tags within quotations :(
    * e.g. if you were evil and had html like this: `<div class="<div>">hello</div>`, it would highlight the `<div>` tag within the quotes
5. hilitor.js is borrowed code with some adaptations to make it specific to highlighting HTML tags
