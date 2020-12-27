from cloudmesh.google.bigquery.Provider import Provider


class Interpreter:

    @staticmethod
    def interprete(arguments):
        googlebigquery = Provider()
        # print(arguments)
        if arguments.delete:
            print(" deepak delete 12/22")
            return ""
        elif arguments.list:
            # print("list project /dataset")
            # googlebigquery list project_id
            # source_id = arguments.get('SOURCE')
            # project id read from yaml file if not passed
            project_id = arguments.get('PROJECT_ID')
            # dataset_id = arguments.get('DATASET_ID')
            # table_id = arguments.get('TABLE_ID')
            # result = googlebigquery.listdatasets()
            # print(result)
            try:
                result = googlebigquery.listdatasets()
                # print(result)
            finally:
                return "Unhandled error"
        elif arguments.listtables:
            # print("listing tables 12/22")
            # googlebigquery list project_id
            # source_id = arguments.get('SOURCE')
            # project_id = arguments.get('PROJECT_ID')
            dataset_id = arguments.get('DATASET_ID')
            # table_id = arguments.get('TABLE_ID')
            # result = googlebigquery.listtables(dataset_id)
            # print(result)
            try:
                result = googlebigquery.listtables(dataset_id)
                # print(result)
            finally:
                return "Unhandled error"
        elif arguments.describetable:
            # googlebigquery list project_id
            # source_id = arguments.get('SOURCE')
            # project_id = arguments.get('PROJECT_ID')
            dataset_id = arguments.get('DATASET_ID')
            table_id = arguments.get('TABLE_ID')
            # result = googlebigquery.describetable(dataset_id, table_id)
            # print(result)
            try:
                result = googlebigquery.describetable(dataset_id, table_id)
                # print(result)
            finally:
                return "Unhandled error"
        else:
            print("Unhandled error")
