findPrefix = function () {
	return db.phones.aggregate([{$group : { _id : "$components.prefix",  n_prefix: {$sum: 1}}}]);
}
