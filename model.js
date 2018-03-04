/**
 * New script file
 *//**
 * Track the trade of a commodity from one trader to another
 * @param {org.acme.model.Trade} trade - the trade to be processed
 * @transaction
 */
function tradeCommodity(trade) {
    trade.commodity.owner = trade.newOwner;
    return getAssetRegistry('org.acme.model.Body_Vitals')
        .then(function (assetRegistry) {
            return assetRegistry.update(trade.commodity);
        });
}
