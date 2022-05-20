import { CompanyTypes, createScraper } from 'israeli-bank-scrapers';
import { OTZAR_HAHAYAL } from './credentials';

(async function () {
    try {
        // read documentation below for available options
        const options = {
            companyId: CompanyTypes.otsarHahayal,
            startDate: new Date('2022-03-01'),
            combineInstallments: false,
            showBrowser: false,
        };

        // read documentation below for information about credentials
        const credentials = OTZAR_HAHAYAL;

        const scraper = createScraper(options);
        const scrapeResult = await scraper.scrape(credentials);

        if (scrapeResult.success) {
            scrapeResult.accounts?.forEach((account) => {
                console.log(`found ${account.txns.length} transactions for account number ${account.accountNumber}`);
            });
        } else {
            throw new Error(scrapeResult.errorType);
        }
    } catch (e: any) {
        console.error(`scraping failed for the following reason: ${e.message}`);
    }
})();