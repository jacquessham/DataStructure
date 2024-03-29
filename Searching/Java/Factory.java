public class Factory {
	
	public Search getSearch(String searchtype) {
		if (searchtype.contains("linear"))
			return new LinearSearch();
		else if (searchtype.contains("binary") && searchtype.contains("recursive"))
			return new BinaryRecursiveSearch();
		else if (searchtype.contains("binary") && searchtype.contains("iterative"))
			return new BinaryIterativeSearch();
		return null;
	}

}
